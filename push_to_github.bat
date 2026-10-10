@echo off
chcp 65001 >nul
title رفع المشروع إلى GitHub (مستودع خاص)
echo =====================================================================
echo         🚀 رفع أطلس الكوزمولوجيا القرآنية إلى GitHub 🚀
echo =====================================================================
echo.
echo المستودع المحلي جاهز وموثق (Git Repository Initialized).
echo.
set /p REPO_URL="أدخل رابط مستودع GitHub (مثال: https://github.com/username/knowledge-lab.git): "

if "%REPO_URL%"=="" (
    echo [خطأ] لم تقم بإدخال الرابط!
    pause
    exit /b
)

echo.
echo جاري ربط المستودع ودفع البيانات...
git remote remove origin 2>nul
git remote add origin %REPO_URL%
git branch -M main
git push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo =====================================================================
    echo ✅ تم رفع المشروع بنجاح إلى GitHub!
    echo =====================================================================
) else (
    echo.
    echo ⚠️ حدث خطأ أثناء الرفع. تأكد من تسجيل دخولك في Git أو توفر الصلاحية.
)
pause
