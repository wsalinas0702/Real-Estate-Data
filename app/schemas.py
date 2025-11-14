"""Pydantic schemas for the real estate application."""
from __future__ import annotations

from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class Property(BaseModel):
    """Represents a property in the catalog."""

    id: int = Field(..., example=1)
    address: str = Field(..., example="123 Maple St")
    city: str = Field(..., example="Austin")
    state: str = Field(..., min_length=2, max_length=2, example="TX")
    zipcode: str = Field(..., min_length=5, max_length=10, example="78701")
    bedrooms: int = Field(..., ge=0, example=3)
    bathrooms: float = Field(..., ge=0, example=2.5)
    square_feet: int = Field(..., ge=0, example=2150)
    lot_size: int = Field(..., ge=0, example=7405)
    property_type: str = Field(..., example="Single Family")
    year_built: int = Field(..., ge=1800, example=2012)
    list_price: int = Field(..., ge=0, example=645000)
    sale_price: int = Field(..., ge=0, example=630000)
    last_sold_date: Optional[date] = Field(None, example="2023-04-21")
    rent_estimate: int = Field(..., ge=0, example=3200)
    neighborhood: str = Field(..., example="Downtown")
    description: str = Field(..., example="Modern home with rooftop deck.")


class PropertySearchFilters(BaseModel):
    """Filters available for property searching."""

    city: Optional[str] = Field(None, description="Filter by city")
    state: Optional[str] = Field(None, description="Filter by state code")
    min_bedrooms: Optional[int] = Field(None, ge=0)
    max_price: Optional[int] = Field(None, ge=0)
    property_type: Optional[str] = Field(None, description="Filter by property type")


class MarketSummary(BaseModel):
    """Aggregated statistics for a collection of properties."""

    city: str
    state: str
    average_list_price: float
    average_rent_estimate: float
    inventory_count: int
