def test_unregister_removes_existing_participant(client):
    # Arrange
    activity_name = "Gym Class"
    participant_email = "john@mergington.edu"
    before_participants = client.get("/activities").json()[activity_name]["participants"]
    before_count = len(before_participants)

    # Act
    response = client.delete(f"/activities/{activity_name}/signup", params={"email": participant_email})

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {participant_email} from {activity_name}"
    participants = client.get("/activities").json()[activity_name]["participants"]
    assert participant_email not in participants
    assert len(participants) == before_count - 1


def test_unregister_unknown_activity_returns_404(client):
    # Arrange
    activity_name = "Unknown Activity"
    participant_email = "someone@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/signup", params={"email": participant_email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_non_registered_participant_returns_404(client):
    # Arrange
    activity_name = "Debate Club"
    participant_email = "not-registered@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity_name}/signup", params={"email": participant_email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not signed up for this activity"
