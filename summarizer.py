# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 04:17:53 2023

@author: sc30a
"""
from summa.summarizer import summarize
from summa import keywords



def summarizer(article_content):
    summary = summarize(article_content, ratio=0.2)
    article_keywords = keywords.keywords(article_content)
    return summary, article_keywords
    
if __name__ == "__main__":
    summary = summarizer("Biogenic gems—often called ‘organic gems’(see Galopim de Carvalho, 2018, for a recent discussion of terminology)—are some of the oldest-used gem materials and have been cherished since pre-history (Hayward, 1990; Tsounis et al., 2010; Charpentier et al., 2012). Rather than having a geological origin, these gem materials—such as pearls, precious corals and ivory (e.g. Figure 1)—are products of biomineralisation processes in which living animals produce mineral substances (e.g. calcium carbonate or calcium phosphate) in terrestrial and marine environments (Mann, 2001). Due to their importance in jewellery and decorative arts, the study of biogenic gem materials constitutes an important part of gemmological research. Natural pearls form in wild molluscs without any assistance, whereas cultured pearls are the result of human intervention on cultivated pearl-producing molluscs (Strack, 2006; Hänni, 2012). Pearls and their shells consist of secretions of different polymorphs of calcium carbonate (CaCO3) such as aragonite, calcite and vaterite. Pearls are sometimes coloured by organic pigments.")
    print(summary)