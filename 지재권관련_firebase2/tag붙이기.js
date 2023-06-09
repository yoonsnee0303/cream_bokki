function readAndProcessFile(fileUrl) {
  return fetch(fileUrl)
    .then((response) => {
      if (!response.ok) {
        throw new Error("Failed to fetch the file");
      }
      return response.text();
    })
    .then((contents) => {
      // Process the file contents
      const lines = contents.split("\n");
      const cellList = [];

      lines.forEach((line) => {
        const cells = line.split(",");
        cells.forEach((cell) => {
          if (cell !== "") {
            cell = "backup/" + cell;
            cellList.push(cell);
          }
        });
      });

      return cellList;
    });
}

const fileUrl = "image.txt";
readAndProcessFile(fileUrl)
  .then((cellList) => {
    console.log(cellList);
    const myCellList = cellList.map(
      (url) => `<a href="${url}" target="_blank">
          <img src="${url}" height="150" width="auto">
      </a>`
    );
    console.log(myCellList);

    var test = document.getElementById("test");
    test.innerHTML = myCellList.join("");
    for (var element of myCellList) {
      console.log(element);
    }
  })
  .catch((err) => {
    console.error("An error occurred:", err);
  });
