async function loadTasks() {
  const res = await fetch('/tasks');
  const tasks = await res.json();
  const container = document.getElementById('container');
  container.innerHTML = '';
  tasks.forEach(task => {
    const li = document.createElement('li');
    li.innerHTML = `${task.task} (${task.date}) <button onclick="deleteTask(${task.id})">❌</button>`;
    container.appendChild(li);
  });
}

async function addTask() {
  const task = document.getElementById('task').value;
  const date = document.getElementById('date').value;
  await fetch('/add-task', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ task, date })
  });
  loadTasks();
}

async function deleteTask(id) {
  await fetch(`/delete-task/${id}`, { method: 'DELETE' });
  loadTasks();
}

window.onload = loadTasks;
