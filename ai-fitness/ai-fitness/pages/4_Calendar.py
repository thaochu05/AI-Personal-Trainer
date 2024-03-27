import streamlit as st
from streamlit_calendar import calendar
import json
from Homepage import set_sidebar_visibility  


st.set_page_config(page_title="Demo for streamlit-calendar", page_icon="📆")



transferred_value = st.session_state.get('transferred_variable')


mode = st.selectbox(
    "Calendar Mode:",
    (
        "daygrid",
        "timegrid",
        "timeline",
        "resource-daygrid",
        "resource-timegrid",
        "resource-timeline",
        "list",
        "multimonth",
    ),
)


events = json.loads(transferred_value)

calendar_resources = [
    {"id": "a", "building": "Building A", "title": "Room A"},
    {"id": "b", "building": "Building A", "title": "Room B"},
    {"id": "c", "building": "Building B", "title": "Room C"},
    {"id": "d", "building": "Building B", "title": "Room D"},
    {"id": "e", "building": "Building C", "title": "Room E"},
    {"id": "f", "building": "Building C", "title": "Room F"},
]
calendar_resources = [
    {"id": "a", "building": "Building A", "title": "Room A"},
    {"id": "b", "building": "Building A", "title": "Room B"},
    {"id": "c", "building": "Building B", "title": "Room C"},
    {"id": "d", "building": "Building B", "title": "Room D"},
    {"id": "e", "building": "Building C", "title": "Room E"},
    {"id": "f", "building": "Building C", "title": "Room F"},
]

calendar_options = {
    "editable": "true",
    "navLinks": "true",
    "resources": calendar_resources,
    "selectable": "true",
}

if "resource" in mode:
    if mode == "resource-daygrid":
        calendar_options = {
            **calendar_options,
            "initialDate": "2023-07-01",
            "initialView": "resourceDayGridDay",
            "resourceGroupField": "building",
        }
    elif mode == "resource-timeline":
        calendar_options = {
            **calendar_options,
            "headerToolbar": {
                "left": "today prev,next",
                "center": "title",
                "right": "resourceTimelineDay,resourceTimelineWeek,resourceTimelineMonth",
            },
            "initialDate": "2023-07-01",
            "initialView": "resourceTimelineDay",
            "resourceGroupField": "building",
        }
    elif mode == "resource-timegrid":
        calendar_options = {
            **calendar_options,
            "initialDate": "2023-07-01",
            "initialView": "resourceTimeGridDay",
            "resourceGroupField": "building",
        }
else:
    if mode == "daygrid":
        calendar_options = {
            **calendar_options,
            "headerToolbar": {
                "left": "today prev,next",
                "center": "title",
                "right": "dayGridDay,dayGridWeek,dayGridMonth",
            },
            "initialDate": "2023-07-01",
            "initialView": "dayGridMonth",
        }
    elif mode == "timegrid":
        calendar_options = {
            **calendar_options,
            "initialView": "timeGridWeek",
        }
    elif mode == "timeline":
        calendar_options = {
            **calendar_options,
            "headerToolbar": {
                "left": "today prev,next",
                "center": "title",
                "right": "timelineDay,timelineWeek,timelineMonth",
            },
            "initialDate": "2023-07-01",
            "initialView": "timelineMonth",
        }
    elif mode == "list":
        calendar_options = {
            **calendar_options,
            "initialDate": "2023-07-01",
            "initialView": "listMonth",
        }
    elif mode == "multimonth":
        calendar_options = {
            **calendar_options,
            "initialView": "multiMonthYear",
        }

state = calendar(
    events= events,
    options=calendar_options,
    custom_css="""
    .fc-event-title {
        color: black; /* Set text color to black */
    }
    .fc-event-past {
        opacity: 0.8;
    }
    .fc-event-time {
        font-style: italic;
    }
    .fc-event-title {
        font-weight: 700;
    }
    .fc-toolbar-title {
        font-size: 2rem;
    }
    """,
    key=mode,
)

if state.get("eventsSet") is not None:
    st.session_state["events"] = state["eventsSet"]

st.write(state)

st.markdown("## API reference")
st.help(calendar)