import { useEffect, useState } from "react";
// const API = "http://localhost:8000";
const API = import.meta.env.VITE_API_URL || "http://localhost:8000";
// Component that displays a list of students and allows
//  adding/deleting students
export default function App() {
  // State for the list of students and the form inputs
  const [students, setStudents] = useState([]);
  const [name, setName] = useState("");
  const [major, setMajor] = useState("");
  // Fetch the list of students from the backend API
  const fetchStudents = async () => {
    const res = await fetch(`${API}/students`);
    const data = await res.json();
    setStudents(data);
  };
  // Fetch students when the component mounts
  useEffect(() => {
    fetchStudents();
  }, []);
  // Function to add a new student by sending a POST request to
  //  the backend
  const addStudent = async (e) => {
    e.preventDefault();
    await fetch(`${API}/students/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, major }),
    });
    setName("");
    setMajor("");
    fetchStudents();
  };
  // Function to delete a student by sending a DELETE request to
  //  the backend
  const deleteStudent = async (id) => {
    await fetch(`${API}/students/${id}`, {
      method: "DELETE",
    });
    fetchStudents();
  };
  // Render the UI
  return (
    <div style={{ padding: 40 }}>
      <h1>🎓 Student Database</h1>

      <form onSubmit={addStudent}>
        <input
          value={name}
          onChange={(e) => setName(e.target.value)}
          placeholder="Name"
          required
        />
        <input
          value={major}
          onChange={(e) => setMajor(e.target.value)}
          placeholder="Major"
          required
        />
        <button type="submit">Add</button>
      </form>

      <ul>
        {students.map((s) => (
          <li key={s.id}>
            {s.name} ({s.major})
            <button onClick={() => deleteStudent(s.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
