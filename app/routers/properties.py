"""API routes for working with property data."""
from __future__ import annotations

from fastapi import APIRouter, HTTPException, Query

from .. import repository
from ..schemas import MarketSummary, Property, PropertySearchFilters

router = APIRouter(prefix="/properties", tags=["properties"])


@router.get("/", response_model=list[Property], summary="List properties")
def list_properties(
    city: str | None = Query(None, description="City name to filter by"),
    state: str | None = Query(None, min_length=2, max_length=2, description="Two letter state code"),
    min_bedrooms: int | None = Query(None, ge=0, description="Minimum number of bedrooms"),
    max_price: int | None = Query(None, ge=0, description="Maximum list price"),
    property_type: str | None = Query(None, description="Property type to filter by"),
) -> list[Property]:
    """Return a filtered list of properties."""

    filters = PropertySearchFilters(
        city=city,
        state=state,
        min_bedrooms=min_bedrooms,
        max_price=max_price,
        property_type=property_type,
    )
    return repository.list_properties(filters)


@router.get("/{property_id}", response_model=Property, summary="Retrieve a property")
def get_property(property_id: int) -> Property:
    """Return a property by its identifier."""

    prop = repository.get_property(property_id)
    if not prop:
        raise HTTPException(status_code=404, detail="Property not found")
    return prop


@router.get(
    "/market-summary",
    response_model=MarketSummary,
    summary="Get market summary",
    description="Aggregate metrics for the selected market using the same filters as the list endpoint.",
)
def get_market_summary(
    city: str = Query(..., description="City to summarize"),
    state: str = Query(..., min_length=2, max_length=2, description="Two letter state code"),
    property_type: str | None = Query(None, description="Optional property type filter"),
) -> MarketSummary:
    """Return average pricing metrics for the requested market."""

    filters = PropertySearchFilters(city=city, state=state, property_type=property_type)
    properties = repository.list_properties(filters)
    summary = repository.summarize_market(properties)
    if summary is None:
        raise HTTPException(status_code=404, detail="No properties found for the requested market")
    return summary
