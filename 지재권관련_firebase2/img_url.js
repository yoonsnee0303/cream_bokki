const fs = require('fs');

const filePaths = ['쿠팡.txt', '신세계.txt', '스마트스토어.txt', '오늘의집.txt', '옥션.txt', '인터파크.txt', '지마켓.txt', '롯데온.txt','11번가.txt']; // 가져올 파일 경로들

let allData = '';

filePaths.forEach(filePath => {
  fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
      console.error('파일을 읽어올 수 없습니다:', err);
      return;
    }

    // 데이터를 이용하여 표 생성하는 로직
    allData += data + '\n';

    // 모든 파일의 데이터를 읽었을 때 마지막에 파일에 저장
    if (filePath === filePaths[filePaths.length - 1]) {
      const outputFilePath = 'image.txt';
      fs.writeFile(outputFilePath, allData, 'utf8', err => {
        if (err) {
          console.error('파일을 저장할 수 없습니다:', err);
          return;
        }
        console.log(outputFilePath, '에 파일이 성공적으로 저장되었습니다.');
      });
    }
  });
});
