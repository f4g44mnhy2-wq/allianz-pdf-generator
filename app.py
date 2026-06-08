from fastapi import FastAPI
from pydantic import BaseModel

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


@app.get("/")
def root():
    return {"status": "running"}

# 🔥 DOČASNÝ TEST ENDPOINT (bez PDF)
@app.post("/generate-pdf")
def generate(data: FormData):

    print("🔥 DORAZILO Z FORMS:")
    print(data.dict())

    return {
        "status": "received",
        "message": "Power Automate connection works"
    }
