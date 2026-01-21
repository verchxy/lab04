import requests

BASE_URL = "https://<your-cloud-run-url>"  # replace after deploy
EXPECTED_MESSAGE = "Welcome Git Action GCP Dev Container!"

def test_root():
    r = requests.get(f"{BASE_URL}/")
    assert r.status_code == 200, f"Expected 200, got {r.status_code}"
    data = r.json()
    assert "message" in data
    assert data["message"] == EXPECTED_MESSAGE
    print("Root endpoint test passed!")

def test_invalid():
    r = requests.get(f"{BASE_URL}/invalid-endpoint")
    assert r.status_code == 404, f"Expected 404, got {r.status_code}"
    print("Invalid endpoint test passed!")

if __name__ == "__main__":
    test_root()
    test_invalid()
    print("All tests passed!")
