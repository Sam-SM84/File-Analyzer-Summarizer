from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer

def summarize(text,sentence_count=5):
    parser = PlaintextParser.from_string(text,Tokenizer('english'))
    summarizer = TextRankSummarizer()

    summary = summarizer(parser.document,sentence_count)
    result = "\n\n".join(str(sentence) for sentence in summary)

    return result