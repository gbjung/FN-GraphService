people=[
  {
    "first_name": "Gyeongbae",
    "id": 1,
    "last_name": "Jung",
    "label": "Gyeongbae Jung",
    "node_labels": [
      "person",
      "korean"
    ],
    "datasource": "FN",
    "source_id": 1
  },
  {
    "first_name": "Kat",
    "id": 2,
    "last_name": "Hong",
    "label": "Kat Hong",
    "node_labels": [
      "person",
      "korean"
    ],
    "datasource": "FN",
    "source_id": 2
  },
  {
    "first_name": "Marly",
    "id": 3,
    "last_name": "Jones",
    "label": "Marly Jones",
    "node_labels": [
      "person",
      "remote employee"
    ],
    "datasource": "FN",
    "source_id": 3
  },
  {
    "first_name": "Joe",
    "id": 4,
    "last_name": "Pak",
    "label": "Joe Park",
    "node_labels": [
      "person",
      "korean",
      "remote employee"
    ],
    "datasource": "FN",
    "source_id": 4
  },
  {
    "first_name": "Tiffany",
    "id": 5,
    "last_name": "Keung",
    "label": "Tiffany Keung",
    "node_labels": [
      "person"
    ],
    "datasource": "FN",
    "source_id": 5
  }
]

organizations=[
  {
    "id": 6,
    "label": "FiscalNote",
    "node_labels": [
      "organization"
    ],
    "datasource": "FN",
    "source_id": 6
  },
  {
    "id": 7,
    "label": "Business Development",
    "node_labels": [
      "organization"
    ],
    "datasource": "FN",
    "source_id": 7
  },
  {
    "id": 8,
    "label": "Research & Development",
    "node_labels": [
      "organization"
    ],
    "datasource": "FN",
    "source_id": 8
  },
  {
    "id": 9,
    "label": "Operations",
    "node_labels": [
      "organization"
    ],
    "datasource": "FN",
    "source_id": 9
  },

]
relationships=[
  {
    "id": 1,
    "source": 1,
    "target": 8,
    "label": 'Part Of',
    "meta": {
      "department": "WebApps"
    }
  },
  {
    "id": 2,
    "source": 2,
    "target": 9,
    "label": 'Part Of',
    "meta": {
      "department": "Facilities"
    }
  },
  {
    "id": 3,
    "source": 3,
    "target": 8,
    "label": 'Part Of',
    "meta": {
      "department": "Research"
    }
  },
  {
    "id": 4,
    "source": 4,
    "target": 8,
    "label": 'Part Of',
    "meta": {
      "department": "Product"
    }
  },
  {
    "id": 5,
    "source": 5,
    "target": 7,
    "label": 'Part Of',
    "meta": {
      "department": "Professional Services"
    }
  },
  {
    "id": 6,
    "source": 7,
    "target": 6,
    "label": 'Department Of'
  },
  {
    "id": 7,
    "source": 8,
    "target": 6,
    "label": 'Department Of'
  },
  {
    "id": 8,
    "source": 9,
    "target": 6,
    "label": 'Department Of'
  },
  {
    "id": 9,
    "source": 1,
    "target": 3,
    "label": 'Coworkers',
    "meta": {
      "context": "Same department"
    }
  },
  {
    "id": 10,
    "source": 1,
    "target": 4,
    "label": 'Coworkers',
    "meta": {
      "context": "Same department",
      "squad": "Stakeholders"
    }
  }
]
