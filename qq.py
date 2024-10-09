from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler

# توكن البوت الخاص بك
TOKEN = "8051076973:AAEhGAhe8ulFe5g9y-7KQyWkugEHwRzV5fc"

# دالة بدء البوت وعرض الأزرار الأساسية
def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("تطبيقات الربح", callback_data='show_apps')],
        [InlineKeyboardButton("شرح البوت", callback_data='bot_info')],
        [InlineKeyboardButton("ابدأ", callback_data='back_to_welcome')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.message:
        update.message.reply_text('مرحباً بك في بوت الربح! هذا هو المكان الذي يمكنك فيه استكشاف تطبيقات لزيادة دخلك. اختر "تطبيقات الربح" لرؤية الخيارات المتاحة:', reply_markup=reply_markup)
    elif update.callback_query:
        update.callback_query.message.reply_text('مرحباً بك في بوت الربح! هذا هو المكان الذي يمكنك فيه استكشاف تطبيقات لزيادة دخلك. اختر "تطبيقات الربح" لرؤية الخيارات المتاحة:', reply_markup=reply_markup)

# دالة عرض معلومات البوت
def bot_info(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    info_text = (
        "### شرح البوت ###\n"
        "هذا البوت يساعدك في الوصول إلى تطبيقات ومواقع متعددة تساعدك في كسب المال عبر الإنترنت. اختر من الخيارات المتاحة لاكتشاف أفضل التطبيقات والطرق التي يمكنك من خلالها زيادة دخلك."
    )

    keyboard = [
        [InlineKeyboardButton("رجوع", callback_data='back_to_welcome')],
        [InlineKeyboardButton("ابدأ", callback_data='back_to_welcome')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(text=info_text, reply_markup=reply_markup)

# دالة عرض قائمة التطبيقات
def show_apps(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    keyboard = [
        [InlineKeyboardButton("برنامج Poll Pay", callback_data='poll_pay_info')],
        [InlineKeyboardButton("برنامج Swagbucks", callback_data='swagbucks_info')],
        [InlineKeyboardButton("برنامج MOBROG", callback_data='mobrog_info')],
        [InlineKeyboardButton("برنامج ySense", callback_data='ysense_info')],
        [InlineKeyboardButton("برنامج Paidwork-App", callback_data='paidwork_info')],
        [InlineKeyboardButton("رجوع", callback_data='back_to_welcome')],
        [InlineKeyboardButton("ابدأ", callback_data='back_to_welcome')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text('اختر تطبيقًا من التطبيقات المتاحة لكسب المال بشكل سهل وممتع:', reply_markup=reply_markup)

# دالة الرجوع إلى القائمة الرئيسية
def back_to_welcome(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    start(update.callback_query, context)

# دالة عرض معلومات برنامج Poll Pay
def poll_pay_info(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    info_text = (
        "### Poll Pay ###\n"
        "Poll Pay هو تطبيق يتيح لك كسب المال من خلال إكمال استطلاعات الرأي المدفوعة. انضم الآن وابدأ بجني الأرباح!\n\n"
        "[رابط التحميل](https://www.pollpay.app/?cmd=sb-register&rb=196810290&cmp=197&cxid=2003-app)"
    )
    
    keyboard = [
        [InlineKeyboardButton("رجوع", callback_data='show_apps')],
        [InlineKeyboardButton("ابدأ", callback_data='back_to_welcome')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(text=info_text, reply_markup=reply_markup)

# دالة عرض معلومات برنامج Swagbucks
def swagbucks_info(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    info_text = (
        "### Swagbucks ###\n"
        "Swagbucks هو تطبيق رائع يوفر لك فرصًا متعددة لكسب المال من خلال إكمال استطلاعات الرأي، التسوق عبر الإنترنت، ومشاهدة الفيديوهات. انضم اليوم وابدأ في تحقيق دخل إضافي!\n\n"
        "[رابط التحميل](https://www.swagbucks.com/?cmd=sb-register&rb=196725232&cmp=197&cxid=2003-app)"
    )
    
    keyboard = [
        [InlineKeyboardButton("رجوع", callback_data='show_apps')],
        [InlineKeyboardButton("ابدأ", callback_data='back_to_welcome')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(text=info_text, reply_markup=reply_markup)

# دالة عرض معلومات برنامج MOBROG
def mobrog_info(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()

    info_text = (
        "### MOBROG ###\n"
        "MOBROG هو تطبيق يمكن أن يساعدك في كسب المال من خلال إكمال الاستطلاعات. سهل الاستخدام وفعال!\n\n"
        "[رابط التسجيل](https://mobrog.com/?membership_promotion=0&i_invite=22779043-67035dc146eee&rkm=38)"
    )

    keyboard = [
        [InlineKeyboardButton("رجوع", callback_data='show_apps')],
        [InlineKeyboardButton("ابدأ", callback_data='back_to_welcome')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(text=info_text, reply_markup=reply_markup)

# دالة عرض معلومات برنامج ySense
def ysense_info(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    info_text = (
        "### ySense ###\n"
        "ySense هو منصة موثوقة لكسب المال عبر الإنترنت من خلال إكمال المهام البسيطة. انضم إلى مجتمعنا واستمتع بتجربة كسب ممتعة!\n\n"
        "[رابط التسجيل](https://www.ysense.com/?rb=196845769)"
    )

    keyboard = [
        [InlineKeyboardButton("رجوع", callback_data='show_apps')],
        [InlineKeyboardButton("ابدأ", callback_data='back_to_welcome')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(text=info_text, reply_markup=reply_markup)

# دالة عرض معلومات برنامج Paidwork-App
def paidwork_info(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    info_text = (
        "### Paidwork-App ###\n"
        "Paidwork-App يوفر لك فرصة كسب المال من خلال إكمال مهام بسيطة مثل استطلاعات الرأي ومشاهدة الفيديوهات. اكتشف كيفية كسب دخل إضافي بسهولة!\n\n"
        "[رابط التسجيل](https://www.paidwork.com/?r=01202955322m)"
    )

    keyboard = [
        [InlineKeyboardButton("رجوع", callback_data='show_apps')],
        [InlineKeyboardButton("ابدأ", callback_data='back_to_welcome')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(text=info_text, reply_markup=reply_markup)

# الدالة الرئيسية لتشغيل البوت
def main() -> None:
    updater = Updater(TOKEN)
    
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CallbackQueryHandler(show_apps, pattern='show_apps'))
    dispatcher.add_handler(CallbackQueryHandler(bot_info, pattern='bot_info'))
    dispatcher.add_handler(CallbackQueryHandler(poll_pay_info, pattern='poll_pay_info'))
    dispatcher.add_handler(CallbackQueryHandler(swagbucks_info, pattern='swagbucks_info'))
    dispatcher.add_handler(CallbackQueryHandler(mobrog_info, pattern='mobrog_info'))
    dispatcher.add_handler(CallbackQueryHandler(ysense_info, pattern='ysense_info'))
    dispatcher.add_handler(CallbackQueryHandler(paidwork_info, pattern='paidwork_info'))
    dispatcher.add_handler(CallbackQueryHandler(back_to_welcome, pattern='back_to_welcome'))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()