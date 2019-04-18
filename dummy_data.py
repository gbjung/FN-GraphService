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
    "source": "FN",
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
    "source": "FN",
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
    "source": "FN",
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
    "source": "FN",
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
    "source": "FN",
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
    "source": "FN",
    "source_id": 6
  },
  {
    "id": 7,
    "full_name": "Business Development",
    "node_labels": [
      "organization"
    ],
    "source": "FN",
    "source_id": 7
  },
  {
    "id": 8,
    "full_name": "Research & Development",
    "node_labels": [
      "organization"
    ],
    "source": "FN",
    "source_id": 8
  },
  {
    "id": 9,
    "full_name": "Operations",
    "node_labels": [
      "organization"
    ],
    "source": "FN",
    "source_id": 9
  },

]
relationships=[
  {
    "id": 1,
    "from_node": 1,
    "to_node": 8,
    "type": 'Part Of',
    "meta": {
      "department": "WebApps"
    }
  },
  {
    "id": 2,
    "from_node": 2,
    "to_node": 9,
    "type": 'Part Of',
    "meta": {
      "department": "Facilities"
    }
  },
  {
    "id": 3,
    "from_node": 3,
    "to_node": 8,
    "type": 'Part Of',
    "meta": {
      "department": "Research"
    }
  },
  {
    "id": 4,
    "from_node": 4,
    "to_node": 8,
    "type": 'Part Of',
    "meta": {
      "department": "Product"
    }
  },
  {
    "id": 5,
    "from_node": 5,
    "to_node": 7,
    "type": 'Part Of',
    "meta": {
      "department": "Professional Services"
    }
  },
  {
    "id": 6,
    "from_node": 7,
    "to_node": 6,
    "type": 'Department Of'
  },
  {
    "id": 7,
    "from_node": 8,
    "to_node": 6,
    "type": 'Department Of'
  },
  {
    "id": 8,
    "from_node": 9,
    "to_node": 6,
    "type": 'Department Of'
  },
  {
    "id": 9,
    "from_node": 1,
    "to_node": 3,
    "type": 'Coworkers',
    "meta": {
      "context": "Same department"
    }
  },
  {
    "id": 10,
    "from_node": 1,
    "to_node": 4,
    "type": 'Coworkers',
    "meta": {
      "context": "Same department",
      "squad": "Stakeholders"
    }
  }
]
