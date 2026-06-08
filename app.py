from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from fillpdf import fillpdfs

app = FastAPI()

# 🟢 pevná firemní data
COMPANY_DATA = {
    "Poskozeny_nazev spolecnosti": "VW Wachal a.s.",
    "Poskozeny_Sidlo": "Tylova 220/17, 767 01 Kroměříž",
    "Pojistna_smlouva_cislo": "5989520147",
    "OZ_Jmeno_prijmeni": "Petr Vaněk",
    "Poskozeny_ICO": "25567225",
    "Cislo_uctu": "1481817349/0800",
}

# 🟢 INPUT z Forms
class FormData(BaseModel):
    jmeno: str = ""
    adresa: str = ""

    popis: str = ""
    znacka: str = ""
    typ: str = ""

    registracni_znacka: str = ""
    vin: str = ""

    rok_vyroby: str = ""
    kilometry: str = ""

    skoda: str = ""
    datum: str = ""

    zpusobeni: str = ""
    vyse_skody_detail: str = ""
    pojistna_udalost_popis: str = ""

    cinnost_na_zaklade: str = ""


def safe(v):
    return "" if v is None else str(v)


@app.get("/")
def root():
    return {"status": "running"}


@app.post("/generate-pdf")
def generate(data: FormData):

    print("🔥 DORAZILO Z FORMS:")
    print(data.model_dump())

    # datum do formátu DD.MM.YYYY
    datum_fmt = ""
    if data.datum:
        try:
            y, m, d = data.datum.split("-")
            datum_fmt = f"{d}.{m}.{y}"
        except Exception:
            datum_fmt = data.datum

    pdf_data = {
        **COMPANY_DATA,

        "Pojisteny_jmeno_prijmeni": safe(data.jmeno),
        "Pojisteny_adresa": safe(data.adresa),

        "poskozena vec_popis": safe(data.popis),
        "poskozena vec_znacka": safe(data.znacka),
        "poskozena vec_typ": safe(data.typ),

        "poskozena vec_registracni_znacka": safe(data.registracni_znacka),
        "poskozena vec_vislo_vin": safe(data.vin),

        "poskozena vec_vyroba": safe(data.rok_vyroby),
        "poskozena vec_kilometry": safe(data.kilometry),

        "Vyse_skody": safe(data.skoda),
        "vyse skody": safe(data.vyse_skody_detail),

        "datum_vzniku_skody": datum_fmt,

        "Zpusobeni_skody": safe(data.zpusobeni),
        "pojistna_udalost_popis": safe(data.pojistna_udalost_popis),

        "ucetnictvi": "vedeme",
    }

    output_path = "/tmp/output.pdf"

    fillpdfs.write_fillable_pdf(
        "formular_allianz.pdf",
        output_path,
        pdf_data
    )

    fillpdfs.write_fillable_pdf(
        "formular_allianz.pdf",
        output_path,
        pdf_data
    )

    return {
        "status": "ok",
        "message": "PDF created",
        "file": "output.pdf"
    }