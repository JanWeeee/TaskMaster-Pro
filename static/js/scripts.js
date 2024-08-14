document.getElementById('task-form').addEventListener('submit', function(e) {
    e.preventDefault();

    const task = {
        title: document.getElementById('title').value,
        description: document.getElementById('description').value,
        due_date: document.getElementById('due_date').value,
    };

    fetch('/api/tasks', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(task),
    })
    .then(response => response.json())
    .then(data => {
        const taskList = document.getElementById('task-list');
        const listItem = document.createElement('li');
        listItem.textContent = `${data.title} - ${data.description} (Due: ${data.due_date})`;
        taskList.appendChild(listItem);
    });
});
