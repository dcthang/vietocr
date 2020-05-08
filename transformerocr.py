from vgg import CNN
import transformer import LanguageTransformer

class TransformerOCR(nn.Module):
    def __init__(self, vocab_size, d_model=512, nhead=8, 
                 num_encoder_layers=6, num_decoder_layers=6, 
                 dim_feedforward=2048, max_seq_length=10000, 
                 pos_dropout=0.1, trans_dropout=0.1):
        
        super(TransformerOCR, self).__init__()
        vocab_size = len(vocab)
        
        self.cnn = CNN()
        self.transformer=LanguageTransformer(vocab_size, d_model, nhead, num_encoder_layers,
                                num_decoder_layers, dim_feedforward, max_seq_length,
                                pos_dropout, trans_dropout)
    
    def forward(self, img, tgt_input, tgt_key_padding_mask):
        """
        Shape:
            - img: (N, C, H, W)
            - tgt_input: (T, N)
            - tgt_key_padding_mask: (N, T)
            - output: b t v
        """
        src = self.cnn(img)
        outputs = self.transformer(src, tgt_input, tgt_key_padding_mask=tgt_key_padding_mask)
        
        return outputs

