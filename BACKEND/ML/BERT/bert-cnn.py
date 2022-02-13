class BERT_Arch(nn.Module):
    def __init__(self, bert):
        super(BERT_Arch, self).__int__()
        self.bert = BertForTokenClassification.from_pretrained(
            '/content/drive/MyDrive/Colab Notebooks/DeepBlue/bert-large-uncased', num_labels=len(tag2idx))

    def forward(self, input_ids, token_type_ids=None, attention_mask=mask)
