# CoAtNet paper analysis

Based on the submission source of truth, `refactor/lean-notebook` at `611f1f4`.
Project comparisons use the saved outputs in `notebooks/engine_fault_classification.ipynb`, checked against `report/report.pdf`. No model training was run for this analysis. The notebook's `fault_recall` is the mean of knock and misfire class recalls, distinct from `fault_detected`.

## Deliverables

- `coatnet-writeup.qmd` / `coatnet-writeup.pdf`: one page of analysis addressing the four rubric questions, followed by a separate references page, as requested.
- `coatnet-slides.qmd` / `coatnet-slides.pdf`: thirteen slides, including the title and a dedicated closing slide, with a planned 13-minute delivery and up to two minutes for discussion. The two additional design-space slides explain the range between convolution and attention. The QMD contains hidden speaker notes; the pacing options below include a shorter ten-minute version. Timings are planning estimates, not a measured rehearsal.
- `../../references/coatnet-2021.pdf`: an unchanged copy of the supplied NeurIPS paper. The supplied PDF has 13 pages and does not include the appendices mentioned in its text. This analysis does not claim to have reviewed those appendices.

The slides focus on the paper; the individual project connection is developed in the write-up. Numerical claims carry table or section locators. The small-data critique is identified as an inference from the evaluated regimes, not a reported negative result.

The presentation tells the conceptual story before introducing notation: local versus global feature gathering, shared versus input-dependent weights, the broader hybrid design space, CoAtNet's choices within that space, a worked relative-attention example, its equation, and the stage layout. Editable TikZ schematics and experimental comparison plots replace most result tables. Blue consistently marks convolution or spatial structure, purple marks adaptive attention, and green marks mixture weights or selected experimental outcomes. The toy scores are explicitly illustrative, experimental plots cite the paper, and zoomed axes are labeled. The design-space schematic is not a numerical interpolation scale or a claim that all illustrated layouts were tested. The paper already credits earlier hybrids and relative-attention methods. The speaker notes explain the examples and methodological caveats; no trained attention maps are implied by the schematics.

The slide PDF uses a GitHub Dark-inspired palette: charcoal canvas (`#0D1117`), header surface (`#161B22`), light text (`#C9D1D9`), muted citations (`#8B949E`), and blue accents (`#58A6FF`).

The write-up uses APA 7 author–date citations, an alphabetical reference list with hanging indents, 12-point Times New Roman, double spacing, 1-inch margins, left-aligned paragraphs with 0.5-inch first-line indents, centered bold headings, and upper-right page numbers. It is a short-assignment adaptation: the user requested one page of analysis plus references, so there is no separate student title page. The prose is condensed to fit the analysis on one page; the original four rubric topics and the lean-branch evidence are preserved. Paper reference metadata comes from the official NeurIPS bibliographic record; the course-report reference links to the exact lean-branch commit.

## Delivery and rehearsal

The opening explicitly frames the data-versus-capacity problem. Slide 6 links the invented numerical example to a spatial sketch and distinguishes learned offset preferences from fixed rules. Slide 9 introduces ImageNet and JFT in plain language, with spoken definitions of transfer and top-1 accuracy before the comparisons. Slide 10 also defines top-1 on screen. Slide 12 presents the remaining small-data question. Slide 13 closes by returning to early convolution, later global attention, and relative position before inviting questions.

| Slide | Topic | Normal pace | Short version |
|---|---|---:|---:|
| 1 | Title and research problem | 0:30 | 0:30 |
| 2 | Two ways to gather information | 1:00 | 0:50 |
| 3 | Complementary strengths | 0:55 | 0:40 |
| 4 | Hybrid design space | 0:55 | 0:40 |
| 5 | CoAtNet's two choices | 0:55 | 0:40 |
| 6 | Spatial and numerical example | 1:45 | 1:15 |
| 7 | Equation from the example | 1:25 | 0:55 |
| 8 | Network layout | 1:10 | 0:50 |
| 9 | Layout experiments and evaluation terms | 1:20 | 1:05 |
| 10 | Two experimental checks | 1:05 | 0:55 |
| 11 | Scaling results | 1:00 | 0:55 |
| 12 | Small-data limitation | 0:30 | 0:20 |
| 13 | Closing answer and questions | 0:30 | 0:25 |
| **Total, before discussion** | | **13:00** | **10:00** |

Rehearse aloud with the PDF before treating either total as achievable. Use the notes as preparation, not a verbatim script. For the shorter version, keep the basic spatial explanation and score-to-share walkthrough, omit the optional exponential calculation, and leave detailed model sizes, normalization caveats, and historical comparisons for questions. Keep the dataset and metric definitions, the illustrative-example disclaimer, and the distinction between an architectural ablation and a cross-paper system comparison. If rehearsal runs long, trim narration before rushing the math example. Leave up to two minutes for discussion in a 15-minute slot.

## Render

From the repository root, with Quarto and a TeX distribution including XeLaTeX and the Metropolis Beamer theme:

```sh
quarto render paper-analysis/coatnet/coatnet-writeup.qmd
quarto render paper-analysis/coatnet/coatnet-slides.qmd
```

The PDFs render alongside their QMD sources. Speaker notes remain editable in the QMD and are hidden in the slide PDF.
