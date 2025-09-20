# Configuration Template for DAX Copilot
# Copy this file to config.py and fill in your actual values

# ==============================================================================
# Azure OpenAI Configuration
# ==============================================================================
# Get these values from your Azure OpenAI resource in the Azure Portal
AZURE_OPENAI_API_KEY = "your-azure-openai-api-key-here"
AZURE_OPENAI_ENDPOINT = "https://your-resource-name.openai.azure.com/"
AZURE_OPENAI_DEPLOYMENT = "your-gpt-deployment-name"
API_VERSION = "2024-02-01"

# ==============================================================================
# Service Principal Configuration  
# ==============================================================================
# Create a service principal with: az ad sp create-for-rbac --name "dax-copilot-sp"
CLIENT_ID = "your-service-principal-client-id"
CLIENT_SECRET = "your-service-principal-client-secret"
TENANT_ID = "your-azure-tenant-id"

# ==============================================================================
# Power BI Configuration
# ==============================================================================
# Power BI workspace and semantic model details
POWERBI_WORKSPACE = "your-powerbi-workspace-name"
SEMANTIC_MODEL = "your-semantic-model-name"

# ==============================================================================
# Optional: RLS Configuration
# ==============================================================================
# Define your RLS rules here
RLS_RULES = {
    "canada_only": {
        "filter": "DimSalesTerritory[Sales Territory Country] = \"Canada\"",
        "description": "Restrict data to Canada only"
    },
    "regional_manager": {
        "filter": "DimSalesTerritory[Sales Territory Region] = \"{region}\"",
        "description": "Regional access based on territory"
    }
}

# ==============================================================================
# Optional: Semantic Model Metadata
# ==============================================================================
# Customize this based on your actual semantic model structure
SEMANTIC_MODEL_METADATA = """
Semantic model metadata:
- Table: FactInternetSales
    • FactInternetSales[SalesAmount] (decimal)
    • FactInternetSales[Transaction Count] (decimal) 
    • FactInternetSales[OrderDate] (date)
- Table: DimSalesTerritory
    • DimSalesTerritory[SalesTerritoryKey] (int)
    • DimSalesTerritory[Sales Territory Region] (string) 
    • DimSalesTerritory[Sales Territory Country] (string)
- Table: DimDate
    • DimDate[DateKey] (int)
    • DimDate[CalendarYear] (int)

Relationships:
- FactInternetSales[SalesTerritoryKey] → DimSalesTerritory[SalesTerritoryKey]
- FactInternetSales[DateKey] → DimDate[DateKey]
"""