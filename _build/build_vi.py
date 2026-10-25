# Vietnamese edition (/vi/). Executed by build_site.py in its namespace (page, ICON, UPDATED_VI, VNI_CHECKOUT, VNI_STORE).
# VNeInvoiceMate is sold in Vietnam only, so it appears only here.

ICON.update({
 'download': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12M7 10l5 5 5-5M5 21h14"/></svg>',
 'check': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 12l2 2 4-4"/><path d="M12 3l8 4v5c0 4.5-3.4 8.3-8 9-4.6-.7-8-4.5-8-9V7l8-4z"/></svg>',
 'bell': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.9 1.9 0 0 0 3.4 0"/></svg>',
 'building': '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M16 6h.01M12 6h.01M12 10h.01M12 14h.01M16 10h.01M16 14h.01M8 10h.01M8 14h.01"/></svg>',
})

# ---------------- Trang chủ ----------------
page('vi/index.html', 'FastMate — công cụ nhỏ giúp làm việc nhanh hơn',
 'FastMate làm những công cụ nhỏ, gọn, tôn trọng quyền riêng tư cho người đi làm. VNeInvoiceMate giúp kế toán tải và kiểm soát hóa đơn điện tử.',
f'''<section class="hero">
  <div class="wrap center" style="max-width:820px">
    <span class="eyebrow">FastMate</span>
    <h1>Công cụ nhỏ giúp công việc của bạn <span style="color:var(--green)">nhanh hơn</span>.</h1>
    <p class="lead" style="margin:0 auto">FastMate làm những công cụ gọn nhẹ cho người đi làm — mỗi công cụ làm tốt một việc, ngay trong trình duyệt bạn đang dùng, và dữ liệu nằm trên máy của bạn.</p>
    <div class="actions" style="justify-content:center">
      <a class="btn btn-primary" href="#san-pham">Xem sản phẩm</a>
      <a class="btn btn-ghost" href="contact.html">Liên hệ</a>
    </div>
  </div>
</section>

<section id="san-pham">
  <div class="wrap">
    <div class="section-head">
      <h2>Sản phẩm</h2>
    </div>
    <div class="grid-2">
      <div class="card product">
        <div class="logo-row"><img src="{{P}}assets/vneinvoicemate-icon.png" alt=""><div><h3>VNeInvoiceMate</h3><span class="tag">Dành cho kế toán</span></div></div>
        <p>Tiện ích Chrome tải hóa đơn đầu vào, đầu ra từ hoadondientu.gdt.gov.vn ra Excel và XML hàng loạt, rồi kiểm tra hóa đơn trước khi kê khai.</p>
        <div class="links"><a class="btn btn-primary btn-sm" href="vneinvoicemate/">Tìm hiểu thêm</a><a class="btn btn-ghost btn-sm" href="vneinvoicemate/#bang-gia">Bảng giá</a></div>
      </div>
      <div class="card product">
        <div class="logo-row"><img src="{{P}}assets/hiremate-icon.png" alt=""><div><h3>HireMate</h3><span class="tag">Dành cho tuyển dụng</span></div></div>
        <p>Tiện ích Chrome cho nhân sự tuyển dụng: xuất hồ sơ LinkedIn™ ra Excel bằng một cú bấm, biết ai sắp chuyển việc và xem lộ trình nghề nghiệp của bất kỳ vị trí nào.</p>
        <div class="links"><a class="btn btn-primary btn-sm" href="hiremate/">Tìm hiểu thêm</a><a class="btn btn-ghost btn-sm" href="hiremate/#bang-gia">Bảng giá</a></div>
      </div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="wrap">
    <div class="section-head"><h2>Cách chúng tôi làm sản phẩm</h2></div>
    <div class="grid-3">
      <div class="card"><div class="icon">{ICON['bolt']}</div><h3>Nhanh ngay từ đầu</h3><p>Có kết quả trong vài giây, ngay trong công cụ bạn đang dùng. Không cần cài đặt phức tạp.</p></div>
      <div class="card"><div class="icon green">{ICON['shield']}</div><h3>Riêng tư</h3><p>Dữ liệu công việc nằm trên máy bạn. Chúng tôi không có máy chủ thu thập dữ liệu đó.</p></div>
      <div class="card"><div class="icon">{ICON['chart']}</div><h3>Thấy điều quan trọng</h3><p>Không chỉ tải dữ liệu — mỗi công cụ giúp bạn nhìn ra việc cần xử lý và quyết định nhanh hơn.</p></div>
    </div>
  </div>
</section>''', lang='vi', alt='index.html')

# ---------------- VNeInvoiceMate ----------------
page('vi/vneinvoicemate/index.html', 'VNeInvoiceMate — Tải hóa đơn điện tử đầu vào, đầu ra ra Excel, XML',
 'Tiện ích Chrome cho kế toán: tải hóa đơn điện tử đầu vào, đầu ra từ hoadondientu.gdt.gov.vn ra Excel, XML hàng loạt; kiểm tra hóa đơn từ 5 triệu, theo dõi hóa đơn bị thay thế, điều chỉnh.',
f'''<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">VNeInvoiceMate · Tiện ích Chrome</span>
      <h1>Tải hóa đơn điện tử hàng loạt, kiểm tra trước khi kê khai.</h1>
      <p class="lead">Đăng nhập hoadondientu.gdt.gov.vn như bình thường, chọn kỳ và bấm tải. VNeInvoiceMate lấy đủ hóa đơn mua vào, bán ra kèm dòng hàng và file XML gốc, xuất Excel gọn gàng — rồi chỉ ra những hóa đơn cần bạn để mắt tới.</p>
      <div class="actions">
        <a class="btn btn-primary" href="{VNI_STORE}" target="_blank" rel="noopener">Thêm vào Chrome — miễn phí</a>
        <a class="btn btn-ghost" href="#bang-gia">Xem bảng giá</a>
      </div>
      <div class="trust"><span>Dữ liệu chỉ lưu trên máy bạn</span><span>Không lưu mật khẩu</span><span>Thiết kế cho đến 500.000 hóa đơn/năm</span></div>
    </div>
    <div class="hero-art" style="padding:12px"><img src="{{P}}assets/vneinvoicemate-hero.jpg" alt="Màn hình danh sách hóa đơn của VNeInvoiceMate" style="border-radius:14px"></div>
  </div>
</section>

<section id="tinh-nang">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Tính năng</span>
      <h2>Bớt sao chép thủ công, bớt sót hóa đơn</h2>
      <p class="lead">Những việc kế toán làm mỗi tháng với hóa đơn điện tử, gom vào một chỗ.</p>
    </div>
    <div class="grid-3">
      <div class="card"><div class="icon">{ICON['download']}</div><h3>Tải đủ, tải hàng loạt</h3><p>Mua vào và bán ra, đủ 3 loại: có mã, không mã, máy tính tiền. Chọn khoảng ngày bất kỳ — tự chia theo tháng, tự chạy tiếp khi hết phiên đăng nhập.</p></div>
      <div class="card"><div class="icon green">{ICON['table']}</div><h3>Dòng hàng và XML gốc</h3><p>Excel giống file của web hoadondientu, thêm cột hóa đơn gốc, lý do điều chỉnh, tổng hợp theo thuế suất; chi tiết dòng hàng hóa, dịch vụ; file XML nén theo tháng.</p></div>
      <div class="card"><div class="icon">{ICON['search']}</div><h3>Lọc như Excel</h3><p>Lọc theo kỳ, ký hiệu, người bán, trạng thái, số tiền (ví dụ &gt;5tr) — tổng tiền của kết quả lọc hiện ngay. Làm mới trạng thái từng hóa đơn.</p></div>
      <div class="card"><div class="icon green">{ICON['check']}</div><h3>Hóa đơn từ 5 triệu</h3><p>Cộng dồn theo người bán trong ngày để biết khoản nào cần chứng từ thanh toán không dùng tiền mặt; đánh dấu đã có ủy nhiệm chi, ghi số chứng từ.</p></div>
      <div class="card"><div class="icon">{ICON['refresh']}</div><h3>Hóa đơn đã kê khai bị sửa</h3><p>Mỗi lần đồng bộ so lại với cổng thuế: báo hóa đơn kỳ cũ mới xuất hiện, hóa đơn đã kê khai nay bị thay thế, điều chỉnh, hủy — gợi ý kỳ cần khai bổ sung.</p></div>
      <div class="card"><div class="icon green">{ICON['trend']}</div><h3>Phát hiện bất thường</h3><p>Chia nhỏ hóa đơn quanh mốc 5 triệu, đơn giá lệch, nhà cung cấp mới giao dịch lớn, hóa đơn ngày nghỉ, nhà cung cấp hay sửa hóa đơn.</p></div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="wrap">
    <div class="section-head"><h2>Dùng thế nào</h2></div>
    <div class="grid-3 steps">
      <div class="step"><h3>Cài và mở</h3><p class="muted">Thêm VNeInvoiceMate vào Chrome, bấm biểu tượng trên thanh công cụ để mở trang làm việc.</p></div>
      <div class="step"><h3>Đăng nhập cổng thuế</h3><p class="muted">Đăng nhập hoadondientu.gdt.gov.vn bằng MST, mật khẩu, captcha như mọi khi. Tiện ích tự nhận ra công ty.</p></div>
      <div class="step"><h3>Chọn kỳ và tải</h3><p class="muted">Chọn mua vào / bán ra, khoảng ngày và loại file. Có thể làm việc khác trong lúc tải, khi xong sẽ có thông báo.</p></div>
    </div>
  </div>
</section>

<section id="bang-gia">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">Bảng giá</span>
      <h2>Tải dữ liệu miễn phí. Nâng cấp khi cần kiểm soát.</h2>
    </div>
    <div class="billing" role="group" aria-label="Kỳ thanh toán">
      <button type="button" data-period="monthly" class="active">Theo tháng</button>
      <button type="button" data-period="yearly">Theo năm <span class="save">−16%</span></button>
    </div>
    <div class="pricing">
      <div class="plan">
        <div><h3>Miễn phí</h3><p class="muted" style="margin:0">Tải và xem hóa đơn</p></div>
        <div class="price">0 đ<small> mãi mãi</small></div>
        <ul>
          <li>Mua vào + bán ra, đủ 3 loại hóa đơn</li>
          <li>Excel danh sách, chi tiết dòng hàng, XML gốc</li>
          <li>Tự chia theo tháng, tự chạy tiếp khi hết phiên</li>
          <li>Xem, lọc, tìm, làm mới trạng thái hóa đơn</li>
          <li>Trang Tổng quan thuế GTGT vào – ra</li>
        </ul>
        <a class="btn btn-ghost" href="{VNI_STORE}" target="_blank" rel="noopener">Thêm vào Chrome</a>
      </div>
      <div class="plan featured">
        <div><h3>Premium</h3><p class="muted" style="margin:0">Cho kế toán làm hằng tháng</p></div>
        <div>
          <div class="price"><span id="pPrice">$1.99</span><small> / tháng</small></div>
          <div class="muted" id="pBilled" style="font-size:14px;margin-top:6px">≈ 52.000 đ · thanh toán hằng tháng</div>
        </div>
        <ul>
          <li>Mọi tính năng miễn phí</li>
          <li><strong>Kiểm tra trước kê khai</strong>: từ 5 triệu (cộng dồn trong ngày), nghi trùng, ngoại tệ, nhiều thuế suất</li>
          <li><strong>Đồng bộ</strong>: báo hóa đơn đã kê khai bị thay thế, điều chỉnh, hủy</li>
          <li><strong>Phân tích bất thường</strong> hóa đơn mua vào</li>
          <li><strong>Nhiều mã số thuế</strong>, báo cáo gộp</li>
        </ul>
        <a class="btn btn-green" href="{VNI_CHECKOUT}" target="_blank" rel="noopener">Mua Premium</a>
      </div>
    </div>
    <p class="billing-note muted">Giá tính bằng USD, thanh toán bằng thẻ; ngân hàng quy đổi sang VND theo tỷ giá của ngân hàng. Hủy gia hạn bất cứ lúc nào. Thanh toán an toàn qua Lemon Squeezy.</p>
  </div>
</section>
<script>
  // Theo tháng $1.99; theo năm $19.99 (≈ $1.67/tháng, −16%).
  (function () {{
    var plans = {{
      monthly: {{ price: '$1.99', unit: ' / tháng', billed: '≈ 52.000 đ · thanh toán hằng tháng' }},
      yearly: {{ price: '$19.99', unit: ' / năm', billed: '≈ 526.000 đ · tương đương $1.67/tháng, tiết kiệm 16%' }}
    }};
    var buttons = document.querySelectorAll('.billing button');
    buttons.forEach(function (b) {{
      b.addEventListener('click', function () {{
        buttons.forEach(function (x) {{ x.classList.toggle('active', x === b); }});
        var p = plans[b.dataset.period];
        document.getElementById('pPrice').textContent = p.price;
        document.getElementById('pPrice').nextElementSibling.textContent = p.unit;
        document.getElementById('pBilled').textContent = p.billed;
      }});
    }});
  }})();
</script>

<section class="section-alt">
  <div class="wrap">
    <div class="section-head"><h2>Câu hỏi thường gặp</h2></div>
    <div class="faq">
      <details><summary>Dữ liệu hóa đơn của tôi được lưu ở đâu?</summary><p>Chỉ trong trình duyệt trên máy của bạn. VNeInvoiceMate không có máy chủ nhận dữ liệu hóa đơn. Bạn có thể xóa dữ liệu của từng công ty hoặc xóa toàn bộ bất cứ lúc nào trong mục Gói &amp; cài đặt.</p></details>
      <details><summary>Có cần đưa mật khẩu cổng thuế cho tiện ích không?</summary><p>Không. Bạn tự đăng nhập hoadondientu.gdt.gov.vn (MST, mật khẩu, captcha) như bình thường. Tiện ích dùng chính phiên đăng nhập đó để tra cứu hóa đơn; không lưu mật khẩu, không tự giải captcha.</p></details>
      <details><summary>Khác gì so với tải trực tiếp trên web hoadondientu?</summary><p>Web chỉ cho tra mỗi lần một tháng và tải XML từng hóa đơn một. VNeInvoiceMate tự chia nhiều tháng, lấy cả dòng hàng và XML hàng loạt, tự chạy tiếp khi hết phiên, và xuất Excel có thêm hóa đơn gốc, lý do điều chỉnh, tổng hợp theo thuế suất.</p></details>
      <details><summary>Tải nhiều hóa đơn có lâu không?</summary><p>Danh sách hóa đơn tải rất nhanh. Dòng hàng và XML thì cổng thuế chỉ cho lấy từng hóa đơn một, nên với vài chục nghìn hóa đơn có thể mất vài giờ — tiện ích ước tính trước, chạy được qua nhiều phiên đăng nhập, và lần sau chỉ tải phần mới.</p></details>
      <details><summary>Có xuất hóa đơn VAT cho gói Premium không?</summary><p>Không. Premium được bán qua Lemon Squeezy (đơn vị bán hàng chính thức); bạn nhận hóa đơn/biên nhận điện tử (invoice/receipt) quốc tế của Lemon Squeezy qua email, không phải hóa đơn điện tử theo quy định Việt Nam.</p></details>
      <details><summary>Hủy Premium thế nào?</summary><p>Trong mục Gói &amp; cài đặt hoặc qua đường link trong email biên nhận. Bạn vẫn dùng Premium đến hết kỳ đã thanh toán. Xem <a href="{{P}}vi/refund.html">Chính sách hoàn tiền</a>.</p></details>
      <details><summary>Kết quả kiểm tra có thay thế tư vấn thuế không?</summary><p>Không. VNeInvoiceMate lấy nguyên trạng dữ liệu từ cổng thuế và chỉ hỗ trợ rà soát; quyết định kê khai vẫn thuộc về bạn và tư vấn thuế của bạn.</p></details>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="cta">
      <div><h2>Tải hóa đơn tháng này trong vài phút.</h2><p>Cài miễn phí. Không cần tạo tài khoản.</p></div>
      <a class="btn btn-ghost" href="{VNI_STORE}" target="_blank" rel="noopener">Thêm VNeInvoiceMate vào Chrome</a>
    </div>
  </div>
</section>''', lang='vi')

exec(io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build_vi_hiremate.py'), encoding='utf-8').read())

# ---------------- Pháp lý ----------------
def legal_vi(path, title, desc, inner, alt):
    page(path, title + ' — FastMate', desc, f'<article class="legal"><h1>{title}</h1><p class="updated">Cập nhật lần cuối: {UPDATED_VI}</p>{inner}</article>', lang='vi', alt=alt)

legal_vi('vi/privacy.html', 'Chính sách quyền riêng tư', 'Cách FastMate và VNeInvoiceMate xử lý dữ liệu của bạn.', '''
<p>Chính sách này giải thích cách FastMate (“chúng tôi”), do Fast Mate vận hành, xử lý thông tin trong các sản phẩm của mình, trong đó có tiện ích Chrome VNeInvoiceMate, và trên trang web này.</p>
<h2>Tóm tắt</h2>
<ul>
  <li>Hóa đơn, dòng hàng và file XML mà VNeInvoiceMate tải về chỉ được lưu <strong>trong trình duyệt trên máy bạn</strong>. Chúng tôi không nhận, không lưu và không bán dữ liệu này.</li>
  <li>VNeInvoiceMate không dùng công cụ phân tích hay cookie theo dõi.</li>
  <li>Khi bạn mua Premium, việc thanh toán do Lemon Squeezy (đơn vị bán hàng chính thức) xử lý.</li>
</ul>
<h2>Dữ liệu VNeInvoiceMate xử lý</h2>
<p>Khi bạn đã đăng nhập hoadondientu.gdt.gov.vn, VNeInvoiceMate đọc cookie đăng nhập của chính trang này để gọi chức năng tra cứu hóa đơn của cổng thuế bằng phiên của bạn. Tiện ích không lưu mật khẩu, không giải captcha và không đọc cookie của trang khác.</p>
<p>Danh sách hóa đơn, chi tiết dòng hàng, file XML, các đánh dấu (ví dụ “đã có chứng từ”, kỳ đã kê khai) và cài đặt được lưu trong bộ nhớ của trình duyệt (IndexedDB và bộ nhớ của tiện ích) trên máy bạn. Dữ liệu chỉ rời khỏi máy khi bạn tự xuất file (Excel, XML) hoặc tự chia sẻ.</p>
<p>Bạn chịu trách nhiệm về việc sử dụng và chia sẻ dữ liệu hóa đơn đã tải, bao gồm tuân thủ quy định về bảo vệ dữ liệu cá nhân (như Nghị định 13/2023/NĐ-CP) và điều khoản của cổng thuế.</p>
<h2>Mua Premium</h2>
<p>Để kích hoạt Premium, VNeInvoiceMate gửi license key và tên thiết bị (ví dụ “VNeInvoiceMate · Win32”) tới dịch vụ license của Lemon Squeezy, và kiểm tra lại vài ngày một lần để gói đã hủy hoặc hết hạn trở về bản miễn phí. Không có dữ liệu hóa đơn nào được gửi đi.</p>
<p>Giao dịch mua do <a href="https://www.lemonsqueezy.com/privacy" target="_blank" rel="noopener">Lemon Squeezy</a> xử lý với tư cách đơn vị bán hàng chính thức (merchant of record); Lemon Squeezy thu thập thông tin thanh toán cần thiết để xử lý giao dịch, thuế và chứng từ. Chúng tôi nhận thông tin đơn hàng (tên, email, license key, trạng thái đơn) để cung cấp Premium và hỗ trợ; chúng tôi không bao giờ thấy đầy đủ thông tin thẻ của bạn.</p>
<h2>Trang web</h2>
<p>Trang web được lưu trữ trên GitHub Pages. GitHub có thể ghi lại dữ liệu kỹ thuật như địa chỉ IP vì mục đích bảo mật; xem chính sách quyền riêng tư của GitHub. Chúng tôi không dùng cookie phân tích hay quảng cáo. Phông chữ được tải từ Google Fonts.</p>
<h2>Quyền mà VNeInvoiceMate sử dụng</h2>
<ul>
  <li><strong>cookies, truy cập hoadondientu.gdt.gov.vn</strong> — đọc cookie đăng nhập của cổng thuế để tra cứu hóa đơn bằng phiên của bạn.</li>
  <li><strong>storage, unlimitedStorage</strong> — lưu hóa đơn, dòng hàng, XML và cài đặt trên máy bạn (một doanh nghiệp có thể có hàng trăm nghìn hóa đơn).</li>
  <li><strong>downloads</strong> — lưu file Excel và XML bạn yêu cầu vào thư mục Tải xuống.</li>
  <li><strong>notifications</strong> — báo khi lượt tải xong, gặp lỗi hoặc cần đăng nhập lại.</li>
  <li><strong>power</strong> — giữ máy không ngủ chỉ trong lúc đang tải dữ liệu.</li>
  <li><strong>truy cập api.lemonsqueezy.com</strong> — chỉ để kích hoạt và kiểm tra license key Premium.</li>
</ul>
<h2>Lựa chọn của bạn</h2>
<p>Bạn có thể xóa dữ liệu của từng công ty, xóa XML đã lưu hoặc xóa toàn bộ dữ liệu trong mục Gói &amp; cài đặt, hoặc gỡ tiện ích (dữ liệu trên máy bị xóa theo). Với dữ liệu mua hàng, hãy liên hệ chúng tôi hoặc Lemon Squeezy.</p>
<h2>Thay đổi</h2>
<p>Chúng tôi có thể cập nhật chính sách này; ngày “cập nhật lần cuối” cho biết phiên bản mới nhất.</p>
<h2>Liên hệ</h2>
<p>Email <a href="mailto:fastmate.support@gmail.com">fastmate.support@gmail.com</a>.</p>''', alt='privacy.html')

legal_vi('vi/terms.html', 'Điều khoản sử dụng', 'Điều khoản sử dụng VNeInvoiceMate và VNeInvoiceMate Premium.', '''
<p>Các điều khoản này áp dụng khi bạn sử dụng tiện ích VNeInvoiceMate và VNeInvoiceMate Premium (“Dịch vụ”) do Fast Mate (“FastMate”, “chúng tôi”) cung cấp. Khi cài đặt hoặc sử dụng Dịch vụ, bạn đồng ý với các điều khoản này.</p>
<h2>1. Dịch vụ</h2>
<p>VNeInvoiceMate giúp bạn tải hóa đơn điện tử của chính doanh nghiệp mình từ hoadondientu.gdt.gov.vn bằng phiên đăng nhập của bạn, lưu trên máy, xuất Excel/XML và rà soát hóa đơn. Tính năng có thể thay đổi theo thời gian.</p>
<h2>2. Trách nhiệm của bạn</h2>
<ul>
  <li>Bạn chỉ dùng Dịch vụ với tài khoản cổng thuế mà bạn được phép sử dụng, và tuân thủ quy định của cổng thuế cũng như pháp luật hiện hành.</li>
  <li>Bạn chịu trách nhiệm về dữ liệu đã tải, xuất và chia sẻ, kể cả dữ liệu cá nhân của người mua/bán trên hóa đơn.</li>
</ul>
<h2>3. Kết quả kiểm tra không phải tư vấn thuế</h2>
<p>Dữ liệu được lấy nguyên trạng từ cổng thuế. Các kết quả kiểm tra, cảnh báo và phân tích (ví dụ hóa đơn từ 5 triệu, nghi trùng, bất thường) chỉ nhằm hỗ trợ rà soát và có thể chưa đầy đủ hoặc chưa chính xác; chúng không thay thế ý kiến tư vấn thuế, kế toán hay pháp lý. Quyết định kê khai là của bạn.</p>
<h2>4. Gói Premium</h2>
<p>Premium được bán qua Lemon Squeezy, đơn vị bán hàng chính thức, và <a href="https://www.lemonsqueezy.com/buyer-terms" target="_blank" rel="noopener">điều khoản người mua</a> của Lemon Squeezy cũng áp dụng cho giao dịch. Gói tự gia hạn cho đến khi bạn hủy; sau khi hủy bạn vẫn dùng đến hết kỳ đã thanh toán. Hoàn tiền theo <a href="refund.html">Chính sách hoàn tiền</a>. Chứng từ thanh toán là hóa đơn/biên nhận quốc tế của Lemon Squeezy, không phải hóa đơn điện tử theo quy định Việt Nam.</p>
<h2>5. Trang web bên thứ ba</h2>
<p>Dịch vụ hoạt động với cổng hoadondientu.gdt.gov.vn mà chúng tôi không kiểm soát; cổng có thể thay đổi hoặc tạm ngừng bất cứ lúc nào, làm một số tính năng tạm thời không dùng được. FastMate và VNeInvoiceMate không liên kết với Tổng cục Thuế hay Bộ Tài chính.</p>
<h2>6. Sở hữu trí tuệ</h2>
<p>Dịch vụ, mã nguồn và thương hiệu thuộc về FastMate. Bạn được cấp quyền sử dụng cá nhân, không chuyển nhượng theo các điều khoản này.</p>
<h2>7. Giới hạn trách nhiệm</h2>
<p>Dịch vụ được cung cấp “nguyên trạng”. Trong phạm vi pháp luật cho phép, FastMate không chịu trách nhiệm về thiệt hại gián tiếp, mất dữ liệu, mất lợi nhuận hay các khoản phạt phát sinh từ việc kê khai; tổng trách nhiệm của chúng tôi không vượt quá số tiền bạn đã trả trong 12 tháng trước khi phát sinh yêu cầu.</p>
<h2>8. Chấm dứt</h2>
<p>Bạn có thể ngừng sử dụng Dịch vụ bất cứ lúc nào. Chúng tôi có thể tạm ngừng quyền truy cập nếu bạn vi phạm các điều khoản này.</p>
<h2>9. Thay đổi</h2>
<p>Chúng tôi có thể cập nhật điều khoản; việc tiếp tục sử dụng sau khi thay đổi đồng nghĩa với việc bạn chấp nhận.</p>
<h2>10. Liên hệ</h2>
<p><a href="mailto:fastmate.support@gmail.com">fastmate.support@gmail.com</a></p>''', alt='terms.html')

legal_vi('vi/refund.html', 'Chính sách hoàn tiền', 'Chính sách hoàn tiền cho gói Premium.', '''
<p>Chúng tôi muốn bạn hài lòng với gói Premium.</p>
<h2>Hoàn tiền trong 14 ngày</h2>
<p>Nếu Premium không phù hợp, bạn có thể yêu cầu hoàn toàn bộ tiền trong <strong>14 ngày</strong> kể từ lần thanh toán đầu tiên, không cần giải thích. Gửi email tới <a href="mailto:fastmate.support@gmail.com">fastmate.support@gmail.com</a> kèm mã đơn hàng, hoặc trả lời email biên nhận của Lemon Squeezy.</p>
<h2>Gia hạn</h2>
<p>Khoản gia hạn được hoàn trong 7 ngày kể từ ngày gia hạn nếu bạn chưa sử dụng Premium kể từ ngày đó. Bạn có thể hủy bất cứ lúc nào để ngừng gia hạn; quyền sử dụng vẫn còn đến hết kỳ đã thanh toán.</p>
<h2>Cách hoàn tiền</h2>
<p>Tiền được Lemon Squeezy, đơn vị bán hàng chính thức, hoàn về phương thức thanh toán ban đầu. Tùy ngân hàng, có thể mất 5–10 ngày làm việc; số tiền nhận lại bằng VND có thể chênh lệch nhỏ do tỷ giá.</p>''', alt='refund.html')

page('vi/contact.html', 'Liên hệ — FastMate', 'Liên hệ FastMate.', '''
<article class="legal">
  <h1>Liên hệ</h1>
  <p class="updated">Chúng tôi thường trả lời trong 1–2 ngày làm việc.</p>
  <div class="grid-2">
    <div class="card"><h3>Hỗ trợ & câu hỏi</h3><p>Câu hỏi về VNeInvoiceMate, gói Premium, thanh toán hoặc hoàn tiền.</p><p style="margin-top:12px"><a class="btn btn-primary btn-sm" href="mailto:fastmate.support@gmail.com">fastmate.support@gmail.com</a></p></div>
    <div class="card"><h3>Quản lý gói</h3><p>Quản lý hoặc hủy gói trong mục Gói &amp; cài đặt của tiện ích, qua đường link trong email biên nhận của Lemon Squeezy, hoặc liên hệ chúng tôi.</p></div>
  </div>
  <p class="note" style="margin-top:24px">Vận hành bởi Fast Mate.</p>
</article>''', lang='vi', alt='contact.html')

# /vneinvoicemate/ → the Vietnamese page (the product exists only in the Vietnamese edition)
_redir = os.path.join(OUT, 'vneinvoicemate', 'index.html')
os.makedirs(os.path.dirname(_redir), exist_ok=True)
io.open(_redir, 'w', encoding='utf-8', newline='\n').write('<!doctype html><meta charset="utf-8"><meta name="robots" content="noindex"><meta http-equiv="refresh" content="0; url=../vi/vneinvoicemate/"><link rel="canonical" href="https://fastmate.io.vn/vi/vneinvoicemate/"><a href="../vi/vneinvoicemate/">VNeInvoiceMate</a>')
