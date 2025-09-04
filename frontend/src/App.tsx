import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";
import { fetchStomps, toggleStomp, type Stomp } from "./api/stomps";
import "./App.css";

function App() {
  const queryClient = useQueryClient();

  // Fetch stomps data
  const { data, isLoading, error } = useQuery({
    queryKey: ["stomps"],
    queryFn: fetchStomps,
  });

  // Toggle stomp mutation
  const toggleStompMutation = useMutation({
    mutationFn: toggleStomp,
    onSuccess: () => {
      // Invalidate and refetch stomps data after successful toggle
      queryClient.invalidateQueries({ queryKey: ["stomps"] });
    },
  });

  const handleToggleStomp = (id: string) => {
    toggleStompMutation.mutate(id);
  };

  if (isLoading) return <div className="loading">Loading stomps...</div>;
  if (error) return <div className="error">Error: {error.message}</div>;

  return (
    <div className="app">
      <header className="app-header">
        <h1>DMX Stomps Controller</h1>
      </header>
      <main className="stomps-container">
        {data?.stomps.map((stomp: Stomp) => (
          <div key={stomp.id} className="stomp-item">
            <h3>{stomp.name}</h3>
            <button
              className={`stomp-button ${stomp.state}`}
              onClick={() => handleToggleStomp(stomp.id)}
              disabled={toggleStompMutation.isPending}
            >
              {stomp.state === "on" ? "ON" : "OFF"}
            </button>
          </div>
        ))}
      </main>
    </div>
  );
}

export default App;
