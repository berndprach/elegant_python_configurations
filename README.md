
# Elegant Python Configuration
*Lightweight, CLI-friendly and Autocomplete-friendly Python Configuration.*

👉 [Read the blog post](https://berndprach.github.io/blog-posts/2025/08/ElegantConfigurationsInPython/).

## ✨ Highlights
 &nbsp; 👓 Readable definitions with clean @dataclass syntax. ([main.py](main.py))  
 &nbsp; ⌨ Autocomplete friendly, avoids typos.  
 &nbsp; 🧼 Minimal parsing logic. ([parsing.py](parsing.py))  
 &nbsp; 🛠️ CLI-friendly. Also support short flags like `-d`.  
 &nbsp; 🧪 Testable. Use direct instantiation for unit tests. ([unittest.py](unittest.py))  


## 🔧 See It in Action:
Define configurations:
```[python]
config1 = parsing.from_command_line(Configuration)
config2 = Configuration(epochs=100)
```

Run this code:
```[bash]
>> python main.py -d "ImageNet" --use-test-set
>> python unittest.py
```


