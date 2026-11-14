import json
from pathlib import Path

FILE_KB = Path(__file__).with_name("kb_belajar.json")

PERTANYAAN = [
    ("tujuan mengingat materi", "Apakah kamu ingin menghafal atau mengingat materi?"),
    ("materi berupa tulisan", "Apakah materi lebih banyak berupa tulisan atau kata-kata?"),
    ("membutuhkan latihan mengingat", "Apakah kamu ingin berlatih mengingat tanpa melihat catatan?"),
    ("materi visual", "Apakah materi lebih mudah dipahami melalui gambar atau diagram?"),
    ("ingin memantau pemahaman", "Apakah kamu ingin mengecek sendiri apakah sudah memahami materi?"),
    ("waktu belajar terbatas", "Apakah waktu belajarmu terbatas?"),
    ("perlu mengatur sumber belajar", "Apakah kamu perlu mengatur waktu, bahan, dan sumber belajar?"),
]

NAMA_FAKTA = {
    "tujuan mengingat materi": "ingin mengingat materi",
    "materi berupa tulisan": "materi berupa tulisan atau kata-kata",
    "membutuhkan latihan mengingat": "membutuhkan latihan mengingat",
    "materi visual": "materi mudah dipahami melalui gambar atau diagram",
    "ingin memantau pemahaman": "ingin mengecek pemahaman",
    "waktu belajar terbatas": "waktu belajar terbatas",
    "perlu mengatur sumber belajar": "perlu mengatur sumber belajar",
}

NAMA_METODE = {
    "metode mnemonic": "Metode Mnemonic (teknik mengingat)",
    "retrieval practice": "Retrieval Practice (latihan mengingat kembali)",
    "representasi visual": "Representasi Visual (gambar dan diagram)",
    "metakognitif": "Metakognitif (mengevaluasi pemahaman diri)",
    "pengelolaan sumber daya belajar": "Pengelolaan Sumber Daya Belajar",
    "retrieval practice dengan monitoring": "Retrieval Practice dengan Monitoring",
}

def baca_kb():
    with FILE_KB.open("r", encoding="utf-8") as file:
        return json.load(file)

def tanya_pengguna():
    fakta_awal = set()
    jawaban_pengguna = []

    print("\nBAGIAN PERTANYAAN")
    print("Jawab y untuk Ya atau t untuk Tidak.\n")

    for nomor, (nama_fakta, pertanyaan) in enumerate(PERTANYAAN, start=1):
        while True:
            jawaban = input(f"{nomor}. {pertanyaan} (y/t) > ").strip().lower()

            if jawaban in ("y", "t"):
                break

            print("Input tidak valid. Masukkan y atau t.")

        jawaban_pengguna.append(jawaban)

        if jawaban == "y":
            fakta_awal.add(nama_fakta)

    return fakta_awal, jawaban_pengguna

def kondisi_terpenuhi(rule, memori):
    syarat = rule.get("jika", [])
    mode = rule.get("mode", "dan")

    if not syarat:
        return False
    if mode == "dan":
        return all(item in memori for item in syarat)
    if mode == "atau":
        return any(item in memori for item in syarat)

    return False

def forward_chaining(fakta_awal, aturan):
    memori = set(fakta_awal)
    aturan_aktif = []
    aturan_dijalankan = set()
    nomor_siklus = 0

    while True:
        aturan_cocok = []

        for rule in aturan:
            hasil = rule.get("maka", "")

            if (rule.get("id") not in aturan_dijalankan and hasil and hasil not in memori and kondisi_terpenuhi(rule, memori)):
                aturan_cocok.append(rule)

        if not aturan_cocok:
            break

        rule = aturan_cocok[0]
        nomor_siklus += 1

        hasil = rule["maka"]
        memori.add(hasil)
        aturan_dijalankan.add(rule["id"])

        aturan_aktif.append({**rule, "_hasil": hasil, "_siklus": nomor_siklus})

    return memori, aturan_aktif, nomor_siklus

def kesimpulan_akhir(aturan_aktif):
    hasil_yang_dipakai_lagi = set()

    for rule in aturan_aktif:
        for syarat in rule.get("jika", []):
            hasil_yang_dipakai_lagi.add(syarat)

    return [
        rule for rule in aturan_aktif
        if rule["_hasil"] not in hasil_yang_dipakai_lagi
    ]

def nama_item(item):
    if item in NAMA_FAKTA:
        return NAMA_FAKTA[item]
    if item in NAMA_METODE:
        return NAMA_METODE[item]

    return item

def cari_aturan_penghasil(fakta, aturan_aktif):
    for rule in aturan_aktif:
        if rule["_hasil"] == fakta:
            return rule

    return None

def tampilkan_alasan(rule, aturan_aktif, fakta_awal, indentasi=4, sudah=None):
    if sudah is None:
        sudah = set()

    syarat_rule = rule.get("jika", [])
    mode = rule.get("mode", "dan")

    if mode == "dan":
        syarat_aktif = syarat_rule
    else:
        syarat_aktif = [
            item for item in syarat_rule
            if item in fakta_awal
            or cari_aturan_penghasil(item, aturan_aktif)
        ]
    for syarat in syarat_aktif:
        aturan_asal = cari_aturan_penghasil(syarat, aturan_aktif)
        spasi = " " * indentasi

        if aturan_asal:
            print(f"{spasi}{nama_item(syarat)} "f"<- {aturan_asal['id']}")

            if aturan_asal["id"] not in sudah:
                sudah.add(aturan_asal["id"])
                tampilkan_alasan(aturan_asal, aturan_aktif, fakta_awal, indentasi + 4, sudah)

        elif syarat in fakta_awal:
            print(f"{spasi}{nama_item(syarat)} (fakta awal)")

def tampilkan_hasil(kb, fakta_awal, jawaban_pengguna, aturan_aktif, jumlah_siklus):
    fakta_ya = [
        NAMA_FAKTA[nama]
        for nama, _ in PERTANYAAN
        if nama in fakta_awal
    ]

    print("\nFAKTA AWAL:")
    if fakta_ya:
        print(", ".join(fakta_ya))
    else:
        print("Tidak ada fakta yang dijawab ya.")

    print("\nPROSES FORWARD CHAINING:")

    if aturan_aktif:
        for rule in aturan_aktif:
            print(
                f"Siklus {rule['_siklus']}: "
                f"{rule['id']} -> {nama_item(rule['_hasil'])}"
            )
    else:
        print("Belum ada aturan yang terpenuhi.")

    print(f"Siklus {jumlah_siklus + 1}: " "tidak ada aturan baru, berhenti.")

    akhir = kesimpulan_akhir(aturan_aktif)

    print("\nKESIMPULAN:")

    if akhir:
        for rule in akhir:
            print(f"- {nama_item(rule['_hasil'])}")
    else:
        print("Tidak ada rekomendasi metode belajar.")

    print("\nALASAN:")

    if akhir:
        for rule in akhir:
            print(f"  {nama_item(rule['_hasil'])} " f"<- {rule['id']}")
            tampilkan_alasan(rule, aturan_aktif, fakta_awal, indentasi=4, sudah=set())
    else:
        print("  Fakta awal belum memenuhi syarat aturan mana pun.")

    print("\nCATATAN BATAS KEBERLAKUAN:")
    print(kb.get("batas", "Aturan merupakan penyederhanaan dari sumber yang digunakan."))

def main():
    try:
        kb = baca_kb()

    except FileNotFoundError:
        print("File kb_belajar.json tidak ditemukan. " "Letakkan file JSON dalam folder yang sama dengan file Python.")
        return

    except json.JSONDecodeError as error:
        print(f"Format kb_belajar.json tidak valid: {error}")
        return

    print("=" * 100)
    print("Rekomendasi Metode Belajar")
    print("Metode : Forward Chaining")
    print("=" * 100)

    fakta_awal, jawaban_pengguna = tanya_pengguna()

    _, aturan_aktif, jumlah_siklus = forward_chaining(
        fakta_awal,
        kb.get("aturan", [])
    )

    tampilkan_hasil(kb, fakta_awal, jawaban_pengguna, aturan_aktif, jumlah_siklus)

if __name__ == "__main__":
    main()