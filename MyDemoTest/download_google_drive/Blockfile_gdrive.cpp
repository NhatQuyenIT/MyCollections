#include <iostream>
#include <curl/curl.h>

// Hàm callback để ghi dữ liệu vào file
size_t WriteCallback(void* contents, size_t size, size_t nmemb, void* userp) {
    FILE* file = (FILE*)userp;
    return fwrite(contents, size, nmemb, file);
}

int main() {
    // Khởi tạo cURL
    CURL* curl = curl_easy_init();
    if (curl) {
        // Mở file để ghi dữ liệu vào
        FILE* file = fopen("downloaded_file.xlsx", "wb");
        if (file) {
            // Đường dẫn đến file trên Google Drive
            const char* url = "https://drive.google.com/uc?export=download&id=1sf4nf79iuEJ5BqF-1RNIQK3hutUy4Nuh";

            // Thiết lập URL và callback
            curl_easy_setopt(curl, CURLOPT_URL, url);
            curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
            curl_easy_setopt(curl, CURLOPT_WRITEDATA, file);

            // Thực hiện yêu cầu tải file
            CURLcode res = curl_easy_perform(curl);
            if (res != CURLE_OK) {
                std::cerr << "Lỗi khi tải file từ Google Drive: " << curl_easy_strerror(res) << std::endl;
            }

            // Đóng file
            fclose(file);
        } else {
            std::cerr << "Không thể mở file để ghi dữ liệu." << std::endl;
        }

        // Giải phóng cURL
        curl_easy_cleanup(curl);
    } else {
        std::cerr << "Không thể khởi tạo cURL." << std::endl;
    }

    return 0;
}// g++ Blockfile_gdrive.cpp -o Blockfile_gdrive -I"C:\curl-8.5.0\include" -L"C:\curl-8.5.0\lib" -lcurl

     