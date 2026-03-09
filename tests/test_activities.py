def test_get_activities_returns_expected_structure(client):
    # Arrange
    required_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert "Chess Club" in activities
    assert "Programming Class" in activities
    assert "Gym Class" in activities

    for details in activities.values():
        assert required_keys.issubset(details.keys())
        assert isinstance(details["participants"], list)
