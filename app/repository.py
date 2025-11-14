"""Data access helpers for the real estate application."""
from __future__ import annotations

from statistics import mean
from typing import Iterable, List, Optional

from . import data
from .schemas import MarketSummary, Property, PropertySearchFilters


def list_properties(filters: Optional[PropertySearchFilters] = None) -> List[Property]:
    """Return properties filtered using the provided filters."""

    def matches_filters(raw: data.RawProperty) -> bool:
        if not filters:
            return True
        if filters.city and raw["city"].lower() != filters.city.lower():
            return False
        if filters.state and raw["state"].lower() != filters.state.lower():
            return False
        if filters.min_bedrooms and raw["bedrooms"] < filters.min_bedrooms:
            return False
        if filters.max_price and raw["list_price"] > filters.max_price:
            return False
        if filters.property_type and raw["property_type"].lower() != filters.property_type.lower():
            return False
        return True

    filtered = [Property(**raw) for raw in data.PROPERTIES if matches_filters(raw)]
    return filtered


def get_property(property_id: int) -> Optional[Property]:
    """Return a property by its unique identifier."""

    for raw in data.PROPERTIES:
        if raw["id"] == property_id:
            return Property(**raw)
    return None


def summarize_market(properties: Iterable[Property]) -> Optional[MarketSummary]:
    """Create a summary for a collection of properties in the same market."""

    properties = list(properties)
    if not properties:
        return None

    avg_list_price = mean(prop.list_price for prop in properties)
    avg_rent = mean(prop.rent_estimate for prop in properties)

    first = properties[0]
    return MarketSummary(
        city=first.city,
        state=first.state,
        average_list_price=avg_list_price,
        average_rent_estimate=avg_rent,
        inventory_count=len(properties),
    )
