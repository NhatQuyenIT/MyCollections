#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <curl/curl.h>

// Khai báo biến lưu trữ đường dẫn tới tệp
char file_path[1024];

// Khai báo biến lưu trữ URL của tệp
char url[1024];

// Hàm tải tệp từ Google Drive
size_t write_callback(void *contents, size_t size, size_t nmemb, void *userp) {
    FILE *file = (FILE *)userp;
    return fwrite(contents, size, nmemb, file);
}

void download_file(const char *file_path, const char *url) {
    // Khởi tạo đối tượng CURL
    CURL *curl = curl_easy_init();
    FILE *file = fopen(file_path, "wb");

    if (curl && file) {
        // Thiết lập URL của tệp
        curl_easy_setopt(curl, CURLOPT_URL, url);

        // Thiết lập callback để ghi dữ liệu vào tệp
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_callback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, file);

        // Thực hiện yêu cầu HTTP
        curl_easy_perform(curl);

        // Đóng tệp sau khi tải xong
        fclose(file);
    }

    // Giải phóng đối tượng CURL
    curl_easy_cleanup(curl);
}

int main() {
    // Nhập đường dẫn tới tệp
    printf("Nhập đường dẫn tới tệp: ");
    fgets(file_path, sizeof(file_path), stdin);
    file_path[strlen(file_path) - 1] = '\0';

    // Tạo URL của tệp
    snprintf(url, sizeof(url), "https://drive.google.com/uc?id=%s", file_path);

    // Tải tệp
    download_file(file_path, url);

    return 0;
}