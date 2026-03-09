def test_signup_adds_new_participant(client):
    # Arrange
    activity_name = "Chess Club"
    participant_email = "new-student@mergington.edu"
    before_count = len(client.get("/activities").json()[activity_name]["participants"])

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": participant_email})

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {participant_email} for {activity_name}"
    participants = client.get("/activities").json()[activity_name]["participants"]
    assert participant_email in participants
    assert len(participants) == before_count + 1


def test_signup_duplicate_participant_returns_400(client):
    # Arrange
    activity_name = "Chess Club"
    participant_email = "michael@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": participant_email})

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"


def test_signup_unknown_activity_returns_404(client):
    # Arrange
    activity_name = "Unknown Activity"
    participant_email = "someone@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity_name}/signup", params={"email": participant_email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"
