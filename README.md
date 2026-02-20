---
title: Theorem Search
emoji: 📚
colorFrom: purple
colorTo: indigo
sdk: docker
app_port: 8501
tags:
- streamlit
pinned: false
short_description: Find math theorems faster.
license: mit
arxiv: 2602.05216
thumbnail: >-
  https://cdn-uploads.huggingface.co/production/uploads/68f6c5227dbd571d889d77d0/EL1gYLps8yOTb-zDDHTTx.png
datasets:
- uw-math-ai/theorem-search-dataset
---

# Theorem Search

Semantic search over 9 million mathematical theorems from arXiv, Stacks Project, ProofWiki, nLab, and more.

**Live demo:** [huggingface.co/spaces/uw-math-ai/theorem-search](https://huggingface.co/spaces/uw-math-ai/theorem-search)

**Paper:** [Semantic Search over 9 Million Mathematical Theorems](https://arxiv.org/abs/2602.05216)

## Deployment

This repo auto-deploys to [Hugging Face Spaces](https://huggingface.co/spaces/uw-math-ai/theorem-search) on every push to `main` via GitHub Actions.

The app requires the following secrets/environment variables configured on the HF Space:
- `AWS_REGION`, `RDS_SECRET_ARN`, `RDS_DB_NAME`, `RDS_READER_HOST`, `RDS_WRITER_HOST` — AWS RDS connection
- `NEBIUS_API_KEY` — embedding API

## Citation

```bibtex
@misc{theoremsearch2026,
      title={Semantic Search over 9 Million Mathematical Theorems},
      author={Luke Alexander and Eric Leonen and Sophie Szeto and Artemii Remizov and Ignacio Tejeda and Giovanni Inchiostro and Vasily Ilin},
      year={2026},
      eprint={2602.05216},
      archivePrefix={arXiv},
      primaryClass={cs.IR}
}
```
