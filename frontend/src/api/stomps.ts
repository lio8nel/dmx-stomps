const API_BASE_URL = "http://localhost:8000";

export interface Stomp {
  id: string;
  name: string;
  state: "on" | "off";
}

export interface StompsResponse {
  stomps: Stomp[];
}

export interface ToggleStompResponse {
  id: string;
  state: "on" | "off";
}

// Fetch all stomps
export const fetchStomps = async (): Promise<StompsResponse> => {
  const response = await fetch(`${API_BASE_URL}/stomps`);
  if (!response.ok) {
    throw new Error("Failed to fetch stomps");
  }
  return response.json();
};

// Toggle a stomp state
export const toggleStomp = async (id: string): Promise<ToggleStompResponse> => {
  const response = await fetch(`${API_BASE_URL}/stomps/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
  });
  if (!response.ok) {
    throw new Error(`Failed to toggle stomp ${id}`);
  }
  return response.json();
};
