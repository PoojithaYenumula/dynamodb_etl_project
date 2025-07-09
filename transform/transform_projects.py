from datetime import datetime

def transform_projects(projects):
    transformed = []

    for proj in projects:
        # Safely convert technologies list → comma string
        techs = proj.get("technologies", [])
        tech_str = ", ".join(techs) if isinstance(techs, list) else str(techs)

        # Handle possible date format issues or missing values
        try:
            start = datetime.strptime(proj["start_date"], "%Y-%m-%d")
            end = datetime.strptime(proj["end_date"], "%Y-%m-%d")
            duration = (end - start).days
        except Exception:
            duration = None  # or 0 if you prefer

        # Safely build transformed record
        transformed.append({
            "project_id": proj.get("project_id", ""),
            "project_name": proj.get("project_name", ""),
            "technologies": tech_str,
            "duration_days": duration,
            "status": proj.get("status", "")
        })

    return transformed
