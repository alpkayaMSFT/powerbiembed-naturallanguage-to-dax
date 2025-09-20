# 🤖 DAX Copilot - Natural Language to DAX with Semantic Kernel

An intelligent Power BI copilot that converts natural language questions into DAX queries using **Semantic Kernel's agentic architecture**. Features advanced Row-Level Security (RLS) support and service principal authentication for enterprise deployments.

![DAX Copilot Architecture](./3%20Steps%20-%20Enhance%20Your%20Power%20BI%20Embed%20Solution%20-%20Custom%20Copilot%20Architecture.png)

## 🚀 Features

- **🧠 Natural Language to DAX**: Convert business questions into optimized DAX queries
- **🔐 Row-Level Security (RLS)**: Automatic security filtering based on user context
- **🏗️ Agentic Architecture**: Modular plugin-based design using Semantic Kernel
- **🔑 Service Principal Auth**: Enterprise-ready authentication for Power BI
- **📊 Direct Query Execution**: Execute DAX queries and return results as DataFrames
- **🎯 Production Ready**: Complete end-to-end workflow with error handling

## 🏗️ Architecture Overview

```
🤖 DAX Copilot Agent
├── 👤 UserContextPlugin → Determines RLS context
├── 🧠 DAXGenerationPlugin → Natural language → DAX  
├── 🔐 AuthenticationPlugin → Service principal tokens
└── 📊 QueryExecutionPlugin → Execute DAX → DataFrame
```

### Plugin Architecture

1. **UserContextPlugin**: Determines if user requires RLS filtering
2. **DAXGenerationPlugin**: Uses Azure OpenAI to generate DAX from natural language
3. **AuthenticationPlugin**: Manages service principal authentication for Power BI
4. **QueryExecutionPlugin**: Executes DAX queries using ADOMD.NET

## 📋 Prerequisites

- **Python 3.8+**
- **Azure OpenAI** service with GPT model deployment
- **Power BI Premium** workspace with semantic model
- **Azure Service Principal** with Power BI permissions
- **ADOMD.NET** client libraries

## 📊 Sample Data

This repository includes **`adventureworksdw2017august2022.pbix`** - a complete Adventure Works sample dataset that you can use to test the DAX Copilot immediately:

- **Pre-configured tables**: FactInternetSales, DimSalesTerritory, DimDate
- **Sample measures**: Revenue, Sales, Transaction Count
- **Ready for RLS**: Includes country-based filtering setup
- **Test queries**: Perfect for validating the copilot functionality

**Quick Start**: Upload this .pbix file to your Power BI workspace to begin testing!

## ⚙️ Setup Instructions

### 1. Clone and Install Dependencies

```bash
git clone https://github.com/alpkayaMSFT/powerbiembedfast.git
cd powerbiembedfast/python-samples-jupyternotebooks
pip install -r requirements.txt
```

### 2. Configure Azure OpenAI

1. Create an Azure OpenAI resource
2. Deploy a GPT model (e.g., `gpt-4`, `gpt-35-turbo`)
3. Note your endpoint, API key, and deployment name

### 3. Create Service Principal

```bash
# Create service principal
az ad sp create-for-rbac --name "dax-copilot-sp" --role contributor

# Note the output:
# - appId (CLIENT_ID)
# - password (CLIENT_SECRET)  
# - tenant (TENANT_ID)
```

### 4. Upload Sample Dataset (Optional but Recommended)

1. **Open Power BI Desktop**
2. **Open the included file**: `adventureworksdw2017august2022.pbix`
3. **Publish to your Power BI workspace**
4. **Note the dataset name** for your configuration

### 5. Configure Power BI Permissions

1. Add service principal to Power BI workspace as **Member**
2. Enable service principal in Power BI admin settings
3. Grant semantic model **Read** permissions

### 6. Update Configuration

Edit the notebook configuration section:

```python
# Azure OpenAI Configuration
AZURE_OPENAI_API_KEY = "your-api-key-here"
AZURE_OPENAI_ENDPOINT = "https://your-resource.openai.azure.com/"
AZURE_OPENAI_DEPLOYMENT = "your-deployment-name"
API_VERSION = "2024-02-01"

# Service Principal Configuration
CLIENT_ID = "your-service-principal-client-id"
CLIENT_SECRET = "your-service-principal-client-secret"
TENANT_ID = "your-azure-tenant-id"

# Power BI Configuration
POWERBI_WORKSPACE = "your-workspace-name"
SEMANTIC_MODEL = "adventureworksdw2017august2022"  # Use the sample dataset
```

## 🎯 Usage Examples

### Basic Query (No RLS)

```python
# Ask a business question
result = await production_dax_copilot_agent(
    question="What is the total sales amount by country?",
    user_type="regular"
)

print(result['dax_query'])
print(result['execution_result'])
```

### RLS-Enabled Query

```python
# Same question with RLS applied
result = await production_dax_copilot_agent(
    question="What is the total sales amount by country?", 
    user_type="rls"  # Applies Canada filter
)

# DAX automatically includes: DimSalesTerritory[Sales Territory Country] = "Canada"
```

### Sample Business Questions

**Adventure Works Dataset Queries:**
- "What is the total revenue for 2013?"
- "Show me sales by country"
- "Which product categories had the highest sales?"
- "What is the average order value by year?"
- "Compare sales between United States and Canada"
- "Show me the top 10 customers by revenue"

## 🔧 Semantic Model Requirements

The copilot expects these standard tables and relationships:

```
Tables:
├── FactInternetSales
│   ├── SalesAmount (decimal)
│   ├── Transaction Count (decimal)
│   └── OrderDate (date)
├── DimSalesTerritory  
│   ├── Sales Territory Region (string)
│   └── Sales Territory Country (string)
└── DimDate
    ├── DateKey (int)
    └── CalendarYear (int)

Relationships:
├── FactInternetSales[SalesTerritoryKey] → DimSalesTerritory[SalesTerritoryKey]
└── FactInternetSales[DateKey] → DimDate[DateKey]
```

## 🔐 Security & RLS Configuration

### RLS Setup in Power BI

1. **Create RLS Role**: Define security filters in Power BI Desktop
2. **Apply Filter**: Example: `DimSalesTerritory[Sales Territory Country] = "Canada"`
3. **Test Role**: Use "View as Role" in Power BI Desktop
4. **Publish Model**: Deploy to Power BI Service

### User Context Mapping

```python
# Configure user context in UserContextPlugin
if user_type.lower() == 'rls':
    context = {
        'user': 'user1@customer.com',
        'rls_filter': 'DimSalesTerritory[Sales Territory Country] = "Canada"',
        'rls_instruction': 'Always apply Canada filter in DAX queries'
    }
```

## 🎨 Customization

### Adding New RLS Rules

Modify the `UserContextPlugin` to support additional RLS scenarios:

```python
def get_user_rls_context(self, user_type: str, user_region: str = None):
    if user_type == 'regional_manager':
        return {
            'rls_filter': f'DimSalesTerritory[Sales Territory Region] = "{user_region}"'
        }
```

### Extending Semantic Model Metadata

Update the `semantic_model_metadata` in `DAXGenerationPlugin` for your model:

```python
self.semantic_model_metadata = """
Your semantic model tables and relationships here...
"""
```

## 🚨 Troubleshooting

### Common Issues

1. **Authentication Failed**
   - Verify service principal permissions
   - Check Power BI workspace access
   - Validate tenant ID

2. **ADOMD.NET Errors**
   - Install ADOMD.NET client libraries
   - Verify .NET Framework compatibility
   - Check connection string format

3. **DAX Generation Issues**
   - Review semantic model metadata
   - Check Azure OpenAI deployment status
   - Validate API key and endpoint

### Debug Mode

Enable detailed logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📊 Performance Optimization

- **Connection Pooling**: Reuse ADOMD.NET connections
- **Token Caching**: Cache service principal tokens
- **Query Optimization**: Review generated DAX for efficiency
- **Model Design**: Optimize semantic model relationships

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Semantic Kernel** team for the agentic framework
- **Power BI** team for ADOMD.NET client libraries
- **Azure OpenAI** for natural language processing capabilities

## 📞 Support

For questions and support:
- Create an [issue](https://github.com/alpkayaMSFT/powerbiembedfast/issues)
- Review the [troubleshooting guide](#-troubleshooting)
- Check [Power BI documentation](https://docs.microsoft.com/power-bi/)

---

⭐ **Star this repo** if you find it helpful!