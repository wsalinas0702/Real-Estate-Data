"""In-memory data storage for sample real estate properties."""
from __future__ import annotations

from datetime import date
from typing import List, TypedDict


class RawProperty(TypedDict):
    """Dictionary representation of a property before Pydantic validation."""

    id: int
    address: str
    city: str
    state: str
    zipcode: str
    bedrooms: int
    bathrooms: float
    square_feet: int
    lot_size: int
    property_type: str
    year_built: int
    list_price: int
    sale_price: int
    last_sold_date: date
    rent_estimate: int
    neighborhood: str
    description: str


PROPERTIES: List[RawProperty] = [
    {
        "id": 1,
        "address": "123 Maple St",
        "city": "Austin",
        "state": "TX",
        "zipcode": "78701",
        "bedrooms": 3,
        "bathrooms": 2.5,
        "square_feet": 2150,
        "lot_size": 7405,
        "property_type": "Single Family",
        "year_built": 2012,
        "list_price": 645000,
        "sale_price": 630000,
        "last_sold_date": date(2023, 4, 21),
        "rent_estimate": 3200,
        "neighborhood": "Downtown",
        "description": "Modern home with rooftop deck and skyline views.",
    },
    {
        "id": 2,
        "address": "890 Pineapple Ave",
        "city": "Orlando",
        "state": "FL",
        "zipcode": "32801",
        "bedrooms": 4,
        "bathrooms": 3.0,
        "square_feet": 2750,
        "lot_size": 9800,
        "property_type": "Single Family",
        "year_built": 2005,
        "list_price": 550000,
        "sale_price": 540000,
        "last_sold_date": date(2022, 11, 2),
        "rent_estimate": 2950,
        "neighborhood": "Thornton Park",
        "description": "Updated kitchen, pool, and outdoor kitchen perfect for entertaining.",
    },
    {
        "id": 3,
        "address": "456 Seaside Blvd Unit 1902",
        "city": "San Diego",
        "state": "CA",
        "zipcode": "92101",
        "bedrooms": 2,
        "bathrooms": 2.0,
        "square_feet": 1295,
        "lot_size": 0,
        "property_type": "Condo",
        "year_built": 2016,
        "list_price": 875000,
        "sale_price": 0,
        "last_sold_date": date(2019, 7, 18),
        "rent_estimate": 3800,
        "neighborhood": "Gaslamp Quarter",
        "description": "Luxury waterfront condo with floor-to-ceiling windows and marina views.",
    },
]
