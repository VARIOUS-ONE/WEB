import torch
from transformers import PreTrainedTokenizerFast, PreTrainedTokenizer
from transformers import BartForConditionalGeneration

tokenizer = PreTrainedTokenizerFast.from_pretrained('gogamza/kobart-summarization')
model = BartForConditionalGeneration.from_pretrained('gogamza/kobart-summarization')

class kobart:
  def kobart_summary(text):
    text = text.replace('\n', ' ')

    raw_input_ids = tokenizer.encode(text)
    input_ids = [tokenizer.bos_token_id] + raw_input_ids + [tokenizer.eos_token_id]
    summary_ids = model.generate(torch.tensor([input_ids]),
                                length_penalty = 0.5,
                                num_beams=8,  
                                max_length=64,  
                                eos_token_id=1)
    output = tokenizer.decode(summary_ids.squeeze().tolist(), skip_special_tokens=True)
    print(output)
    return output

#kobart_summary(text)