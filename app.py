@app.post("/generate-pdf")
def generate(data: FormData):

    print("🔥 START")

    print("📄 TEMPLATE EXISTS:", os.path.exists("formular_allianz.pdf"))

    try:
        fillpdfs.write_fillable_pdf(
            "formular_allianz.pdf",
            "/tmp/output.pdf",
            {}
        )
        print("✅ PDF GENERATED STEP DONE")

    except Exception as e:
        print("❌ ERROR:", str(e))
        return {"status": "error", "message": str(e)}

    return {"status": "ok"}