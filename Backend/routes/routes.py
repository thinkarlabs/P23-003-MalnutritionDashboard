from Backend.model.model import AaganwadiSummary
from typing import List
from fastapi import APIRouter
from Backend.config.database import AangawadiSummaryCollection

from typing import Union

aaganwadi_summary = APIRouter()

# FastAPI endpoint to retrieve the summary of an Aaganwadi program
@aaganwadi_summary.get("/aaganwadi/summary/{aaganwadi_id}")
async def get_aaganwadi_summary(aaganwadi_id: str):
    """
    Get the Aaganwadi program summary for the given ID.
    :aaganwadi_id (str): The ID of the Aaganwadi program to get the summary for.
    :Returns:AaganwadiSummary: An instance of the AaganwadiSummary class containing the summary data.
    If the program summary is not found in the database, returns an instance with all counts set to 0.
    """
    # Query the MongoDB database for the Aaganwadi program summary
    summary = AangawadiSummaryCollection.find_one({"_id": aaganwadi_id})

    # If summary is None, return 0 for all categories
    if summary is None:
        return AaganwadiSummary()

    # Calculate the change count compared to the last week
    sam_change = summary.get("SAMCountThisWeek", 0) - \
        summary.get("SAMCountLastWeek", 0)
    mam_change = summary.get("MAMCountThisWeek", 0) - \
        summary.get("MAMCountLastWeek", 0)
    normal_change = summary.get(
        "NormalCountThisWeek", 0) - summary.get("NormalCountLastWeek", 0)

    # Initialize a new instance of the AaganwadiSummary class with the summary data
    aaganwadi_summary = AaganwadiSummary(
        TotalChildCount=summary.get("TotalChildCount", 0),
        SAMCountThisWeek=summary.get("SAMCountThisWeek", 0),
        MAMCountThisWeek=summary.get("MAMCountThisWeek", 0),
        NormalCountThisWeek=summary.get("NormalCountThisWeek", 0),
        SAMChangeCount=sam_change,
        MAMChangeCount=mam_change,
        NormalChangeCount=normal_change
    )

    # Return the AaganwadiSummary instance as the response
    return aaganwadi_summary
