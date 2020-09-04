mkdir -p ~/.streamlit                                                            
                                                                                 
echo "[server]                                                                   
headless = true                                                                  
port = $PORT                                                                     
enableCORS = false                                                               
" > ~/.streamlit/config.toml 
pipenv run streamlit run mlf_ext_data_fred_api.py