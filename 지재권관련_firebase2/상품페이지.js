const fs = require("fs");
const path = require("path");
const XLSX = require("xlsx");

// 파일 경로들을 배열로 저장합니다.
const filePaths = [
  "C:/Users/Data2/OneDrive/바탕 화면/firebase2/11번가_index.xlsx",
  "C:/Users/Data2/OneDrive/바탕 화면/firebase2/롯데온_index.xlsx",
  "C:/Users/Data2/OneDrive/바탕 화면/firebase2/스마트스토어_index.xlsx",
  "C:/Users/Data2/OneDrive/바탕 화면/firebase2/신세계_index.xlsx",
  "C:/Users/Data2/OneDrive/바탕 화면/firebase2/오늘의집_index.xlsx",
  "C:/Users/Data2/OneDrive/바탕 화면/firebase2/옥션_index.xlsx",
  "C:/Users/Data2/OneDrive/바탕 화면/firebase2/인터파크_index.xlsx",
  "C:/Users/Data2/OneDrive/바탕 화면/firebase2/지마켓_index.xlsx",
  "C:/Users/Data2/OneDrive/바탕 화면/firebase2/쿠팡_index.xlsx"
];

// 파일 경로들을 순회하며 처리합니다.
filePaths.forEach((filePath) => {
  const workbook = XLSX.readFile(filePath);
  const sheetName = workbook.SheetNames[0];
  const worksheet = workbook.Sheets[sheetName];
  const jsonData = XLSX.utils.sheet_to_json(worksheet, { header: 1 });

  // 데이터를 바로 출력합니다.
  const rows = jsonData.map((row) => row.join(""));
  const content = rows.join("\n");

  const outputFilePath = path.join(__dirname, "상품페이지.txt");

  fs.writeFile(outputFilePath, content, "utf8", (err) => {
    if (err) {
      console.error("파일을 쓰는 중에 오류가 발생했습니다:", err);
      return;
    }

    console.log("파일이 성공적으로 저장되었습니다.");
  });
});
