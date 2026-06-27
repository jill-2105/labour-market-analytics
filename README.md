# Dataset Branch - Data Cleaning and Preprocessing

This branch contains the data cleaning and preprocessing work for the project **Canadian Labour Market Analytics: Employment, Wages & Sustainable Development**. The goal of this branch is to convert the four source datasets into clean, analysis-ready files for dashboard development in Apache Superset.
## Datasets Processed

The preprocessing pipeline covers four datasets used in the project:

- **Statistics Canada - Labour Force Survey (LFS):** long-term employment and unemployment trends by industry and province.
- **Statistics Canada - SEPH:** average weekly earnings by industry and province.
- **OECD Annual Wages Dataset:** international annual wage comparisons using PPP-adjusted USD.
- **UN SDG Goal 8 Dataset:** SDG 8.5.1, 8.5.2, and 8.6.1 indicators for selected peer countries.

## Cleaning Goals

The cleaning work focused on making the data easier to analyze, easier to join across sources, and more suitable for interactive dashboard filtering. The main purpose was to keep only fields that directly support the project’s analytical stories on employment trends, wages, SDG 8 benchmarking, and sustainability-related labour outcomes.

## Key Cleaning Decisions

### 1. Kept only analysis-relevant columns
For each dataset, non-essential metadata, release fields, technical IDs, and unused descriptive columns were removed so the final files stay smaller, clearer, and easier to work with in Superset. This was done to reduce noise and keep only the fields needed for filtering, grouping, comparison, and chart building.

### 2. Preserved common analytical dimensions
Columns related to **time**, **geography**, **industry**, and **value fields** were retained wherever applicable because these dimensions are central to the dashboard design and cross-dataset comparison. For the Canadian datasets, province and NAICS fields were preserved to support regional and sector analysis.

### 3. Filtered the UN dataset to only required SDG 8 indicators
The raw UN SDG dataset contains many unrelated indicators and a very large number of extra breakdown fields. It was filtered to include only:
- **8.5.1** - average hourly earnings
- **8.5.2** - unemployment rate
- **8.6.1** - youth NEET rate

These were selected because they directly support the project’s SDG 8 benchmarking and labour market analysis goals.

### 4. Filtered the UN dataset to selected comparison countries
The SDG dataset was restricted to the project’s selected peer-country set so it aligns with the OECD wage comparison dataset and supports consistent international benchmarking. The selected countries include Canada, the United States, the United Kingdom, Germany, France, Italy, Japan, the Republic of Korea, Mexico, Türkiye, and Australia.

### 5. Retained disaggregation fields only when analytically useful
For the UN SDG dataset, the retained columns include:
- `Goal`, `Target`, `Indicator`
- `SeriesCode`, `SeriesDescription`
- `GeoAreaCode`, `GeoAreaName`
- `TimePeriod`, `Value`, `Units`
- `Sex`, `Age`, `Location`
- `Nature`, `Observation Status`

These were kept because they support comparisons by country, year, sex, age group, and indicator meaning, while also preserving basic data quality interpretation.

### 6. Removed unnecessary breakdown columns
The raw UN dataset contains many specialized fields such as occupation type, education level, hazard type, transport mode, disease categories, policy domains, and many other breakdown dimensions that are not relevant to this project’s dashboard scope. These were excluded to avoid clutter and to keep the cleaned dataset focused on the project’s actual analytical questions.

### 7. Preserved data quality flags
Fields such as `Nature` and `Observation Status` were kept because they show whether values are reported, estimated, or otherwise flagged for interpretation. These fields are important because the project requirements expect SDG data quality status to remain visible in analysis rather than being silently discarded.

### 8. Excluded null or low-value fields when appropriate
The `location` field was previously identified as mostly null across retained rows and was treated as a low-value field for the final filtered SDG dataset design. In general, columns with little analytical use, heavy sparsity, or no role in the dashboard were removed to improve dataset clarity and reduce preprocessing complexity.

## Why these decisions were made

These cleaning decisions were made to support four practical goals:

- **Usability:** simpler files are easier to inspect, debug, and document.
- **Performance:** smaller and more focused datasets are easier to load into PostgreSQL and Apache Superset.
- **Relevance:** only the fields needed for project questions and dashboard filters were preserved.
- **Reproducibility:** the preprocessing logic is explicit and can be rerun from the raw source files.

## Current Output

The preprocessing work produces cleaned, analysis-ready files that are structured for:
- trend analysis over time
- province and industry comparisons
- international benchmarking
- SDG 8 indicator analysis
- later dashboard integration in Apache Superset.

## Current Branch Purpose

This branch is dedicated to Jill’s dataset cleaning and preprocessing work, including:
- filtering raw datasets
- reducing columns
- preserving required analytical dimensions
- preparing final cleaned outputs for dashboard use
- documenting cleaning decisions and assumptions.