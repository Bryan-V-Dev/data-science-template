# {{ cookiecutter.project_name }}

By: {{ cookiecutter.project_author_name}}

{{ cookiecutter.project_description }}

## Installation guide

Please read [install.md](install.md) for details on how to set up this project.

## Project Organization

.
├── {{cookiecutter.project_module_name}}          <= Source code for use in this project.
│   │
│   ├── data                                      <= Scripts to download or generate data sets.
│   │   └── make_dataset.py                       
│   │
│   ├── features                                  <= Scripts to turn raw data into features for modeling.
│   │   └── build_features.py
│   │
│   ├── models                                    <= Scripts to train models and then use trained models to make predictions.
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   ├── utils                                     <= Scripts to help with common tasks.
│   │   └── paths.py
│   │
│   └── visualization                             <= Scripts to create exploratory and results oriented visualizations.
│       └── visualize.py
│
├── data                                          
│   ├── external                                  <= Data from third party sources.
│   │
│   ├── interim                                   <= Intermediate data that has been transformed.
│   │
│   ├── processed                                 <= The final, canonical data sets for modeling.
│   │
│   └── raw                                       <= The original, immutable data dump.
│
├── models                                        <= Trained and serialized models, model predictions, or model summaries.
│
├── notebooks                                     <= (for ordering) Naming **1.0-jqp-data-exploration**.
│   
├── references                                    <= Data dictionaries, manuals, and all other explanatory materials.
│   
├── reports                                       <= Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures                                   <= Generated graphics and figures to be used in reporting.
│
├── .gitignore
│
├── .here                                         <= File that will stop the search if none of the other criteria.
│
├── environment.yml                               <= The requirements file for reproducing the analysis environment.
│
├── install.md                                    <= Detailed instructions to set up this project.
│
├── LICENSE
│
├── README.md                                     <= The top-level README for developers using this project.
│
├── setup.py                                      <= Makes project pip installable (pip install -e .) │                                                    so {{ cookiecutter.project_module_name }} can be imported.
│
└── tasks.py                                      <= Invoke with commands like **notebook**.
