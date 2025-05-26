# User & Transaction Graph Environment

A comprehensive system to visualize relationships between users, companies, and transactions using graph database technology. This tool helps identify connections and patterns in financial transactions and business relationships.

![Graph Visualization](docs/images/graph-visualization.png)

## Features

- **Graph Database Integration**: Neo4j or AWS Neptune for storing complex relationship data
- **Interactive Visualization**: Dynamic, web-based graph visualization using Cytoscape.js
- **Multiple Node Types**: Users, companies, and transactions with distinct visual styling
- **Rich Relationship Types**: Business relationships (Parent-Child, Director, Shareholder) and transaction flows
- **Advanced Filtering**: Filter by node types and relationship categories
- **Detailed Information Panel**: View comprehensive details about any node in the graph
- **Search Functionality**: Find specific nodes by name, ID, or attributes
- **Multiple Layout Options**: Different algorithms for optimal graph visualization
- **Export Capability**: Save graph visualizations as images
- **Responsive Design**: Works on desktop and mobile devices

## Prerequisites

- Python 3.8+
- Neo4j Database (4.4+)
- Docker (optional, for running Neo4j in a container)

## Setup Instructions

### 1. Clone the repository

```bash
git clone <repository-url>
cd User\&TransactionGraphEnviroment
```

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up Neo4j

#### Option 1: Using Docker

```bash
docker run \
    --name neo4j \
    -p 7474:7474 -p 7687:7687 \
    -e NEO4J_AUTH=neo4j/password \
    -e NEO4J_ACCEPT_LICENSE_AGREEMENT=yes \
    neo4j:latest
```

#### Option 2: Install Neo4j locally

Download and install Neo4j Desktop from [Neo4j's website](https://neo4j.com/download/).

### 5. Configure environment variables

Create a `.env` file in the project root with the following content:

```
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=password
```

Adjust the values according to your Neo4j setup.

### 6. Initialize the database with test data

```bash
python -m app.utils.init_db
```

### 7. Run the backend API

```bash
python -m app.main
```

The API will be available at http://localhost:8000.

### 8. Run the frontend visualization

```bash
# Install Flask if not already installed
pip install flask

# Run the frontend server
cd frontend
python server.py
```

The web interface will be available at http://localhost:5001.

Alternatively, you can use the provided script:

```bash
./run_frontend.sh
```

## API Documentation

Once the application is running, you can access the API documentation at http://localhost:8000/docs.

### Available Endpoints

#### User and Transaction Management
- `POST /api/users`: Add or update user information
- `POST /api/transactions`: Add or update transaction details
- `GET /api/users`: List all users
- `GET /api/transactions`: List all transactions

#### Relationship Management
- `GET /api/relationships/user/{id}`: Fetch all connections of a user
- `GET /api/relationships/transaction/{id}`: Fetch all connections of a transaction
- `POST /api/business-relationships`: Create a new business relationship between two users
- `GET /api/business-relationships/user/{id}`: Fetch all business relationships of a user
- `POST /api/detect-relationships`: Detect and create relationships between users and transactions

## Running Tests

```bash
pytest
```

## Web Visualization Interface

The web-based visualization interface provides an interactive way to explore the relationships between users, companies, and transactions.

### Features

- Interactive graph visualization using Cytoscape.js
- Filter nodes and relationships by type
- Search for specific nodes
- View detailed information about nodes and their connections
- Multiple layout options for better visualization
- Export graph as an image
- Responsive design for different screen sizes

### Navigation

- **Zoom**: Use the mouse wheel or the zoom buttons in the toolbar
- **Pan**: Click and drag on the background
- **Select Node**: Click on a node to view its details
- **Reset View**: Click the "Reset View" button to fit the graph to the screen

### Filtering

Use the checkboxes in the sidebar to filter:
- Node types (Users, Companies, Transactions)
- Relationship types (Parent-Child, Director, Shareholder, etc.)

### Searching

Enter a search term in the search box and click the search button to find nodes by name or label.

### Node Details Panel

When you click on a node, a details panel appears showing:

- **For Users**: Name, email, phone, address, and other personal information
- **For Companies**: Company name, address, industry, tax ID, directors, and shareholders with ownership percentages
- **For Transactions**: Amount, currency, purpose, timestamp, sender, and receiver information

### Visual Styling

- **Users**: Blue circular nodes
- **Companies**: Green rectangular nodes
- **Transactions**: Yellow diamond-shaped nodes
- **Relationships**: Color-coded edges based on relationship type

## Recent Improvements

### UI Enhancements
- **Improved Transaction Display**: Transactions now show proper names and purposes instead of generic identifiers
- **Enhanced Node Details**: Better formatting for complex data like shareholders and directors
- **Permanent Sidebar**: Removed hamburger menu for easier access to filters and controls
- **Visual Differentiation**: Clearer visual distinction between users, companies, and transactions
- **Responsive Layout**: Better support for different screen sizes

### Data Visualization
- **Formatted Shareholder Data**: Shareholders now display with proper percentage badges
- **Better Transaction Relationships**: Improved display of transaction senders and receivers
- **Enhanced Node Labels**: More descriptive labels for all node types
- **Color-Coded Relationships**: Easier identification of relationship types through consistent color coding

## Relationship Types

The system automatically detects and creates the following relationship types:

### User-to-User Relationships
- `SHARED_EMAIL`: Users sharing the same email address
- `SHARED_PHONE`: Users sharing the same phone number
- `SHARED_ADDRESS`: Users sharing the same physical address
- `SHARED_PAYMENT_METHOD`: Users sharing the same payment method

### User-to-Transaction Relationships
- `SENT`: User sent money in a transaction
- `RECEIVED_BY`: User received money in a transaction

### Transaction-to-Transaction Relationships
- `LINKED_TO`: Transactions linked by shared IP address or device ID

### Business Relationships
- `PARENT_OF`: Parent company relationship to a subsidiary
- `SUBSIDIARY_OF`: Subsidiary relationship to a parent company
- `DIRECTOR_OF`: Director relationship to a company
- `SHAREHOLDER_OF`: Shareholder relationship to a company
- `LEGAL_ENTITY_OF`: Legal entity relationship between a person and a company
- `COMPOSITE`: A composite relationship that combines multiple relationship types for stronger connection analysis
