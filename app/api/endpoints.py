from fastapi import APIRouter, HTTPException, Depends
from app.models.models import User, Transaction, BusinessRelationship
from app.database.operations import GraphOperations
from app.api.graph_data import GraphDataService
from typing import List, Dict, Any

router = APIRouter()

@router.post("/users", response_model=Dict[str, Any])
async def create_user(user: User):
    """
    Create a new user in the graph database
    """
    result = GraphOperations.create_user(user)
    if not result:
        raise HTTPException(status_code=500, detail="Failed to create user")

    # Detect and create relationships after adding a new user
    GraphOperations.detect_and_create_relationships()

    return {"message": "User created successfully", "user_id": user.id}

@router.post("/transactions", response_model=Dict[str, Any])
async def create_transaction(transaction: Transaction):
    """
    Create a new transaction in the graph database
    """
    result = GraphOperations.create_transaction(transaction)
    if not result:
        raise HTTPException(status_code=500, detail="Failed to create transaction")

    # Detect and create relationships after adding a new transaction
    GraphOperations.detect_and_create_relationships()

    return {"message": "Transaction created successfully", "transaction_id": transaction.id}

@router.get("/users", response_model=List[Dict[str, Any]])
async def get_all_users():
    """
    Get all users from the graph database
    """
    users = GraphOperations.get_all_users()
    return users

@router.get("/transactions", response_model=List[Dict[str, Any]])
async def get_all_transactions():
    """
    Get all transactions from the graph database
    """
    transactions = GraphOperations.get_all_transactions()
    return transactions

@router.get("/relationships/user/{user_id}", response_model=Dict[str, Any])
async def get_user_relationships(user_id: str):
    """
    Get all relationships of a user
    """
    relationships = GraphOperations.get_user_relationships(user_id)
    if not relationships:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")

    return relationships

@router.get("/relationships/transaction/{transaction_id}", response_model=Dict[str, Any])
async def get_transaction_relationships(transaction_id: str):
    """
    Get all relationships of a transaction
    """
    relationships = GraphOperations.get_transaction_relationships(transaction_id)
    if not relationships:
        raise HTTPException(status_code=404, detail=f"Transaction with ID {transaction_id} not found")

    return relationships

@router.post("/business-relationships", response_model=Dict[str, Any])
async def create_business_relationship(relationship: BusinessRelationship):
    """
    Create a new business relationship between two users
    """
    result = GraphOperations.create_business_relationship(relationship)
    if not result:
        raise HTTPException(status_code=500, detail="Failed to create business relationship")

    return {
        "message": "Business relationship created successfully",
        "source_id": relationship.source_id,
        "target_id": relationship.target_id,
        "relationship_type": relationship.relationship_type
    }

@router.get("/business-relationships/user/{user_id}", response_model=Dict[str, Any])
async def get_business_relationships(user_id: str):
    """
    Get all business relationships of a user
    """
    relationships = GraphOperations.get_business_relationships(user_id)
    if not relationships:
        raise HTTPException(status_code=404, detail=f"User with ID {user_id} not found")

    return relationships

@router.post("/detect-relationships", response_model=Dict[str, Any])
async def detect_relationships():
    """
    Detect and create relationships between users and transactions
    """
    GraphOperations.detect_and_create_relationships()
    return {"message": "Relationships detected and created successfully"}

@router.get("/graph-data")
async def get_graph_data():
    """
    Get all nodes and edges from the graph database in a format suitable for visualization
    """
    from fastapi.responses import JSONResponse

    # Create a simple function to convert Neo4j DateTime objects to strings
    def convert_neo4j_types(obj):
        from neo4j.time import DateTime
        from datetime import datetime

        if isinstance(obj, DateTime):
            # Convert Neo4j DateTime to string
            return f"{obj.year}-{obj.month:02d}-{obj.day:02d}T{obj.hour:02d}:{obj.minute:02d}:{obj.second:02d}"
        elif isinstance(obj, datetime):
            # Convert Python datetime to string
            return obj.isoformat()
        elif isinstance(obj, dict):
            # Recursively convert dictionary values
            return {key: convert_neo4j_types(value) for key, value in obj.items()}
        elif isinstance(obj, list):
            # Recursively convert list items
            return [convert_neo4j_types(item) for item in obj]
        else:
            # Return other types as is
            return obj

    # Get the data and convert Neo4j types
    data = GraphDataService.get_graph_data()
    converted_data = convert_neo4j_types(data)

    return JSONResponse(content=converted_data)
