from transformers import M2M100Config, M2M100ForConditionalGeneration, M2M100Tokenizer


model = M2M100ForConditionalGeneration.from_pretrained('facebook/m2m100_418M')
tokenizer = M2M100Tokenizer.from_pretrained('facebook/m2m100_418M', src_lang="en", tgt_lang="jp")


def translate(src_text: str, src_lang: str, tgt_lang: str) -> str:
    tokenizer.src_lang = src_lang

    model_inputs = tokenizer(src_text, return_tensors="pt")
    generated_tokens = model.generate(
        **model_inputs,
        forced_bos_token_id=tokenizer.get_lang_id(tgt_lang))
    result = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)

    return result
