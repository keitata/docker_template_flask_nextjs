export default function Test() {
  return (
    <main>
      <button
        onClick={() => {
          fetch("http://localhost:8000/ping").then(async (r) => {
            console.log(await r.json());
          });
        }}
      >
        ping
      </button>
      <br />
      <button
        onClick={() => {
          fetch("http://localhost:8000/samples").then(async (r) => {
            console.log(await r.json());
          });
        }}
      >
        samples
      </button>
    </main>
  );
}
