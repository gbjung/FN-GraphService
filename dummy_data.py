people=[
  {
    "first_name": "Gyeongbae",
    "id": 1,
    "last_name": "Jung",
    "full_name": "Gyeongbae Jung",
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
    "full_name": "Kat Hong",
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
    "full_name": "Marly Jones",
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
    "full_name": "Joe Park",
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
    "full_name": "Tiffany Keung",
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
    "full_name": "FiscalNote",
    "node_labels": [
      "organization"
    ],
    "datasource": "FN",
    "source_id": 6
  },
  {
    "id": 7,
    "full_name": "Business Development",
    "node_labels": [
      "organization"
    ],
    "datasource": "FN",
    "source_id": 7
  },
  {
    "id": 8,
    "full_name": "Research & Development",
    "node_labels": [
      "organization"
    ],
    "datasource": "FN",
    "source_id": 8
  },
  {
    "id": 9,
    "full_name": "Operations",
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
    "type": 'Part Of',
    "meta": {
      "department": "WebApps"
    }
  },
  {
    "id": 2,
    "source": 2,
    "target": 9,
    "type": 'Part Of',
    "meta": {
      "department": "Facilities"
    }
  },
  {
    "id": 3,
    "source": 3,
    "target": 8,
    "type": 'Part Of',
    "meta": {
      "department": "Research"
    }
  },
  {
    "id": 4,
    "source": 4,
    "target": 8,
    "type": 'Part Of',
    "meta": {
      "department": "Product"
    }
  },
  {
    "id": 5,
    "source": 5,
    "target": 7,
    "type": 'Part Of',
    "meta": {
      "department": "Professional Services"
    }
  },
  {
    "id": 6,
    "source": 7,
    "target": 6,
    "type": 'Department Of'
  },
  {
    "id": 7,
    "source": 8,
    "target": 6,
    "type": 'Department Of'
  },
  {
    "id": 8,
    "source": 9,
    "target": 6,
    "type": 'Department Of'
  },
  {
    "id": 9,
    "source": 1,
    "target": 3,
    "type": 'Coworkers',
    "meta": {
      "context": "Same department"
    }
  },
  {
    "id": 10,
    "source": 1,
    "target": 4,
    "type": 'Coworkers',
    "meta": {
      "context": "Same department",
      "squad": "Stakeholders"
    }
  }
]
