# CoAtNet paper analysis

Based on the submission source of truth, `refactor/lean-notebook` at `611f1f4`.
Project comparisons use the saved outputs in `notebooks/engine_fault_classification.ipynb`, checked against `report/report.pdf`. No model training was run for this analysis. The notebook's `fault_recall` is the mean of knock and misfire class recalls, distinct from `fault_detected`.

## Deliverables

- `coatnet-writeup.qmd` / `coatnet-writeup.pdf`: one page of analysis addressing the four rubric questions, followed by a separate references page, as requested.
- `coatnet-slides.qmd` / `coatnet-slides.pdf`: thirteen slides, including the title and a dedicated closing slide, with a planned 13-minute delivery and up to two minutes for discussion. The two additional design-space slides explain the range between convolution and attention. The QMD contains hidden speaker notes; the pacing options below include a shorter ten-minute version. Timings are planning estimates, not a measured rehearsal.
- `coatnet-slides-v2.qmd` / `coatnet-slides-v2.pdf`: separate ten-slide revision, organized around inductive bias, with a 8:10 main-presentation pacing estimate and two results charts. The original deck above is preserved as a reference. See the v2 section below for its figure selections and pacing.
- `../../references/coatnet-2021.pdf`: an unchanged copy of the supplied NeurIPS paper. The supplied PDF has 13 pages and does not include the appendices mentioned in its text. This analysis does not claim to have reviewed those appendices.

The slides focus on the paper; the individual project connection is developed in the write-up. Numerical claims carry table or section locators. The small-data critique is identified as an inference from the evaluated regimes, not a reported negative result.

The presentation tells the conceptual story before introducing notation: local versus global feature gathering, shared versus input-dependent weights, the broader hybrid design space, CoAtNet's choices within that space, a worked relative-attention example, its equation, and the stage layout. Editable TikZ schematics and experimental comparison plots replace most result tables. Blue consistently marks convolution or spatial structure, purple marks adaptive attention, and green marks mixture weights or selected experimental outcomes. The toy scores are explicitly illustrative, experimental plots cite the paper, and zoomed axes are labeled. The design-space schematic is not a numerical interpolation scale or a claim that all illustrated layouts were tested. The paper already credits earlier hybrids and relative-attention methods. The speaker notes explain the examples and methodological caveats; no trained attention maps are implied by the schematics.

The original slide PDF uses a GitHub Dark-inspired palette: charcoal canvas (`#0D1117`), header surface (`#161B22`), light text (`#C9D1D9`), muted citations (`#8B949E`), and blue accents (`#58A6FF`).

The write-up uses APA 7 author–date citations, an alphabetical reference list with hanging indents, 12-point Times New Roman, double spacing, 1-inch margins, left-aligned paragraphs with 0.5-inch first-line indents, centered bold headings, and upper-right page numbers. It is a short-assignment adaptation: the user requested one page of analysis plus references, so there is no separate student title page. The prose is condensed to fit the analysis on one page; the original four rubric topics and the lean-branch evidence are preserved. Paper reference metadata comes from the official NeurIPS bibliographic record; the course-report reference links to the exact lean-branch commit.

## Original deck: delivery and rehearsal

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

## V2: inductive bias and interpretable results

V2 uses the [Carbonfox palette](https://github.com/EdenEast/nightfox.nvim/blob/main/lua/nightfox/palette/carbonfox.lua), matching the colors in the local Carbonfox configuration: charcoal canvas (`#161616`), header surface (`#252525`), light text (`#F2F4F8`), secondary text (`#B6B8BB`), and borders (`#535353`). Convolution stays blue (`#78A9FF`), attention purple (`#BE95FF`), and CoAtNet results green (`#25BE6A`); teal (`#08BDBA`) and pink (`#FF7EB6`) distinguish the other accents and results. Secondary text uses the brighter foreground shade for readability.

The revised story is assumptions → tested layouts → selected architecture → results → limits. The opening reuses the original convolution-versus-attention feature-map visual with a brief comparison of their spatial assumptions: convolution builds in local structure, while attention leaves more spatial relationships to be learned. A short flow diagram then explains the authors' convolution-first prior and the computational reason for delaying global attention. The tested-layout slide defines T as relative attention, highlights the selected C-C-T-T row, and shows the ViT comparator as a patch stem followed by one relative-attention stack. The next slide names the selected layout and labels C, C, T, T inside its four main stages; supporting explanation remains in the speaker notes. The reported layout search includes four ordered multistage variants and the ViT-style relative-attention comparator; alternating stages and attention-before-convolution layouts are explicitly outside that search. The conclusion is limited to the tested regimes.

The worked-example slide has been removed from v2; the architecture slide retains the compact caption “Inside attention: content match + relative-position bias.” The speaker notes for slides 4 and 5 briefly incorporate the supporting layout and position-bias findings, respectively. Their full before/after comparisons (81.78% → 82.39% for layout and 85.3% → 85.7% for position bias) remain in those speaker notes, with their separate experimental settings explicit. The deck ends with the conclusion and questions; there is no backup slide. The architecture now leads directly into two large charts separating model-size comparisons from results across data scales:

- **Figure 1, accuracy versus model size:** adapts the five model-family curves from the paper's Figure 3, with ImageNet-21K pretraining and final ImageNet evaluation. Approximate (parameters in millions, top-1 percent) points recovered from the PDF's vector paths: CoAtNet [(75, 87.3), (167, 87.9), (275, 88.56)]; EfficientNetV2 [(24, 85.0), (55, 86.1), (121, 86.8)]; Swin [(88, 86.0), (197, 86.4)]; CvT [(20, 83.3), (32, 84.9), (277, 87.7)]; ViT [(87, 84.6), (304, 85.3)]. Lines connect reported points within each family. Figure-derived positions are approximate; the source figure places CoAtNet's middle point at about 167M, whereas Table 4 lists 168M. The hidden notes document the extraction and axis mapping. The single HaloNet point and the JFT-pretrained horizontal ViT reference are omitted to keep the chart focused on family curves with ImageNet-21K pretraining. Evaluation sizes and training recipes differ, so this replaces the earlier 384-only Table 4 selection and remains a system comparison. Parameters measure model size, not the paper's empirical capacity concept.
- **Figure 2, accuracy across data scales:** fourteen selected results from Tables 4–5, colored by family and labeled by variant. At 1.28M images: CoAtNet-3 (86.0%), EfficientNetV2-L (85.7%), Swin-B (84.2%), NFNet-F5 (86.0%). At 12.7M: CoAtNet-4 + PT-RA-E150 (88.56%), EfficientNetV2-L (86.8%), Swin-B (86.0%), ViT-L/16 (85.3%). At 300M: CoAtNet-5 (89.77%), ViT-L/16 (87.76%), ViT-H/14 (88.55%), NFNet-F4+ (89.2%). At 3B: CoAtNet-7 (90.88%) and ViT-G/14 (90.45%). All scores are final ImageNet top-1 accuracy. The image-count axis is logarithmic; point coordinates are not jittered. CoAtNet-3 and NFNet-F5 share a point at 1.28M/86.0%, shown with a green center and pink ring. Unconnected points distinguish these changing systems from a controlled learning curve. Evaluation resolutions, model sizes, datasets, and training recipes vary. Exact source rows, parameter counts, resolutions, selection rationale, and the distinction between previous-work benchmarks and the authors' controlled experiments are documented in the speaker notes.

Both charts use zoomed accuracy axes and remain editable in the QMD. The title slide credits the paper; detailed citations and source-table references are retained in the hidden speaker notes instead of repeated slide footers. Slides 6–7 give more space to the graphs and retain their axis labels and essential dataset context. Slide 8 gathers the model-size and data-scale takeaways and states that model variants, data, training recipes, and evaluation sizes differ. Figure numbers used here and in the notes belong to the deck, not the original paper. The model-size chart now follows the paper's Figure 3, including its strongest CoAtNet endpoint; the interpretation slide explicitly notes the differing evaluation sizes and training recipes. Slide 7 compares five model families and retains separate points because both the model and dataset change; it does not imply that all baselines were retrained under one protocol. The limitations slide retains the untested small-data question alongside the untested stage orders.

| Slide | Topic | Planned time |
|---|---|---:|
| 1 | Title and research question | 0:20 |
| 2 | Inductive bias in visual learning | 1:00 |
| 3 | Why convolution before attention? | 0:55 |
| 4 | What the authors actually compared | 1:05 |
| 5 | Selected layout: C-C-T-T | 0:55 |
| 6 | Accuracy versus model size | 0:45 |
| 7 | Accuracy across data scales | 0:45 |
| 8 | What the results show | 0:50 |
| 9 | What remains untested? | 0:55 |
| 10 | Closing answer and questions | 0:40 |
| **Total, before discussion** | | **8:10** |

The v2 QMD includes hidden `::: notes` with transitions, exact plotted values, and optional methodological detail. The timing is an estimate and needs an aloud rehearsal; the full notes are preparation, not a verbatim script. The presentation leaves about 1:50 of breathing room within a ten-minute slot. Slide 10 closes the deck and invites questions.

## Render

From the repository root, with Quarto and a TeX distribution including XeLaTeX and the Metropolis Beamer theme:

```sh
quarto render paper-analysis/coatnet/coatnet-writeup.qmd
quarto render paper-analysis/coatnet/coatnet-slides.qmd
quarto render paper-analysis/coatnet/coatnet-slides-v2.qmd
```

The PDFs render alongside their QMD sources. Speaker notes remain editable in the QMD and are hidden in the slide PDF.
