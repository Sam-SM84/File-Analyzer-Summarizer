from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

from transformers import T5Tokenizer, T5ForConditionalGeneration

def summarize_textRank(text,paragraph_count=5):
    parser = PlaintextParser.from_string(text,Tokenizer('english'))
    summarizer = TextRankSummarizer()

    summary = summarizer(parser.document,paragraph_count)
    result = "\n\n".join(str(sentence) for sentence in summary)

    return result

def summarize_T5(text):
    model_name = "t5-small"
    tokenizer = T5Tokenizer.from_pretrained(model_name)
    model = T5ForConditionalGeneration.from_pretrained(model_name)

    text = "summarize : " + text
    token_id = tokenizer.encode(
    text,
    return_tensors="pt",
    max_length=512,
    truncation=True
)

    summary_id = model.generate(
    token_id,
    max_length=60,
    min_length=20,
    num_beams=4,
    )
    #print(type(tokenizer.decode(summary_id[0])))
    return tokenizer.decode(summary_id[0], skip_special_tokens=True)

