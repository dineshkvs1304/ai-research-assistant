from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline


def load_llm():

    model_name = "google/flan-t5-base"

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    generator = pipeline(
        "text2text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=200
    )

    def llm(prompt):

        result = generator(prompt)

        answer = result[0]["generated_text"]

        return [{"generated_text": answer}]

    return llm