from task_helpers import filter_by_assignee, group_by_status


def test_group_by_status_groups_correctly():
    tasks = [
        {"id": 1, "status": "open"},
        {"id": 2, "status": "done"},
        {"id": 3, "status": "open"},
    ]
    groups = group_by_status(tasks)
    assert {t["id"] for t in groups["open"]} == {1, 3}
    assert {t["id"] for t in groups["done"]} == {2}


def test_group_by_status_handles_missing():
    groups = group_by_status([{"id": 1}])
    assert groups["unknown"] == [{"id": 1}]


def test_filter_by_assignee():
    tasks = [
        {"id": 1, "assignee": "alice"},
        {"id": 2, "assignee": "bob"},
        {"id": 3, "assignee": "alice"},
    ]
    assert {t["id"] for t in filter_by_assignee(tasks, "alice")} == {1, 3}


def test_filter_by_assignee_no_matches():
    assert filter_by_assignee([{"id": 1, "assignee": "alice"}], "carol") == []
