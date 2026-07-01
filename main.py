#!/usr/bin/env python3
"""
Gato Agente - AI Agent for AI Video Tools Hub
Executes every 6 hours to monitor, edit content, and improve the platform
"""

import os
import sys
import logging
import schedule
import time
from datetime import datetime
from dotenv import load_dotenv

# Import modules
from modules.monitoring import MonitoringModule
from modules.editing import EditingModule
from modules.platform_improvement import PlatformImprovementModule
from modules.audience_growth import AudienceGrowthModule
from modules.email_sender import EmailSender

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('gato_agente.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class GatoAgente:
    """Main AI Agent for platform management"""
    
    def __init__(self):
        """Initialize the agent with all modules"""
        logger.info("🐱 Inicializando Gato Agente...")
        
        self.monitoring = MonitoringModule()
        self.editing = EditingModule()
        self.improvement = PlatformImprovementModule()
        self.growth = AudienceGrowthModule()
        self.email_sender = EmailSender()
        
        logger.info("✅ Gato Agente inicializado correctamente")
    
    def run_monitoring(self):
        """Priority 1: Monitor platform health"""
        logger.info("🔍 [PRIORIDAD 1] Iniciando monitoreo...")
        try:
            self.monitoring.check_server_health()
            self.monitoring.check_errors()
            self.monitoring.generate_report()
            logger.info("✅ Monitoreo completado")
        except Exception as e:
            logger.error(f"❌ Error en monitoreo: {e}")
    
    def run_editing(self):
        """Priority 2: Edit photos and videos"""
        logger.info("✏️ [PRIORIDAD 2] Iniciando edición de contenido...")
        try:
            self.editing.download_sample_images()
            self.editing.apply_transformations()
            self.editing.update_gallery()
            logger.info("✅ Edición completada")
        except Exception as e:
            logger.error(f"❌ Error en edición: {e}")
    
    def run_improvement(self):
        """Priority 3: Improve platform"""
        logger.info("🚀 [PRIORIDAD 3] Mejorando plataforma...")
        try:
            self.improvement.analyze_performance()
            self.improvement.suggest_improvements()
            self.improvement.implement_changes()
            logger.info("✅ Mejoras aplicadas")
        except Exception as e:
            logger.error(f"❌ Error en mejoras: {e}")
    
    def run_growth(self):
        """Priority 3 (continued): Audience growth strategy"""
        logger.info("📈 [PRIORIDAD 3] Estrategia de crecimiento...")
        try:
            self.growth.analyze_trends()
            self.growth.optimize_seo()
            self.growth.improve_ux()
            logger.info("✅ Estrategia de crecimiento aplicada")
        except Exception as e:
            logger.error(f"❌ Error en crecimiento: {e}")
    
    def run_all_tasks(self):
        """Execute all tasks in priority order"""
        logger.info("=" * 60)
        logger.info(f"🐱 GATO AGENTE - Ejecución: {datetime.now()}")
        logger.info("=" * 60)
        
        self.run_monitoring()
        self.run_editing()
        self.run_improvement()
        self.run_growth()
        
        logger.info("=" * 60)
        logger.info("✅ Ciclo completo finalizado")
        logger.info("=" * 60)
        
        # Send logs via email
        self.send_logs_email()
    
    def send_logs_email(self):
        """Send logs via email"""
        logger.info("📧 Enviando logs por email...")
        try:
            # Read latest logs
            with open('gato_agente.log', 'r') as f:
                logs = f.read()
            
            # Send email
            self.email_sender.send_logs(logs)
        except Exception as e:
            logger.error(f"❌ Error enviando logs: {e}")
    
    def schedule_tasks(self):
        """Schedule tasks to run every 6 hours"""
        schedule.every(6).hours.do(self.run_all_tasks)
        
        logger.info("📅 Tareas programadas cada 6 horas")
        logger.info("⏰ Próxima ejecución: en 6 horas")
        
        # Run immediately on startup
        self.run_all_tasks()
        
        # Keep scheduler running
        while True:
            schedule.run_pending()
            time.sleep(60)

def main():
    """Main entry point"""
    try:
        agent = GatoAgente()
        agent.schedule_tasks()
    except KeyboardInterrupt:
        logger.info("🛑 Gato Agente detenido por usuario")
        sys.exit(0)
    except Exception as e:
        logger.error(f"❌ Error fatal: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
