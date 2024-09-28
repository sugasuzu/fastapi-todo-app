export default function Home() {
  return (
    <div className="max-w-lg mx-auto p-4">
      <h1 className="text-3xl font-bold text-center mb-4">Todo List</h1>
      <ul className="bg-white shadow-md rounded-lg">
        <li className="flex justify-between items-center p-4 border-b">
          <div className="flex items-center">
            <input type="checkbox" className="mr-5" />
            <div>
              <h2 className="font-semibold">title</h2>
              <p className="text-gray-600">description</p>
            </div>
          </div>
            <button className="bg-red-500 text-white py-1 px-3 rounded">
              Delete
            </button>
        </li>
      </ul>

      <h2 className="text-xl font-semibold mt-6 mb-2">Add a new Todo</h2>
      <div className="flex flex-col gap-2">
        <input type="text" className="border rounded p-2" placeholder="Title" />
        <input
          type="text"
          className="border rounded p-2"
          placeholder="Description"
        />
        <button className="bg-blue-500 text-white py-2 rounded">
          Add Todo
        </button>
      </div>
    </div>
  );
}
